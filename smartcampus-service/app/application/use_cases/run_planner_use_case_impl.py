import time

from pathlib import Path
from datetime import datetime
from app.application.use_cases.run_planner_use_case import RunPlannerUseCase
from app.application.use_cases.generate_pddl_use_case import GeneratePDDLUseCase
from app.infrastructure.pddl.pddl_filesystem_service import PDDLFilesystemService
from app.infrastructure.planner.docker_planner_execution_service import DockerPlannerExecutionService

class RunPlannerUseCaseImpl(RunPlannerUseCase):
  def __init__(
    self,
    generate_pddl_use_case: GeneratePDDLUseCase,
    filesystem_service: PDDLFilesystemService,
    planner_service: DockerPlannerExecutionService,
    parser: "PDDLPlanParser",
    scheduler: "IScheduler"
  ):
    self._generate_pddl = generate_pddl_use_case
    self._filesystem = filesystem_service
    self._planner = planner_service
    self._parser = parser
    self._scheduler = scheduler

  def execute(self, input_data) -> dict:
    job_id = self._planner.create_job()
    start_time = time.time()
      
    try:
      problem_pddl = self._generate_pddl.execute(input_data)
        
      self._filesystem.setup_job(job_id)
      self._filesystem.write_domain(job_id)
      self._filesystem.write_problem(job_id, problem_pddl)

      execution_result = self._planner.run(job_id)

      if not execution_result.get("success"):
        error_detail = execution_result.get("stderr") or execution_result.get("output")
        raise Exception(f"Planner execution error: {error_detail}")

      plan_path = Path(self._filesystem.get_plan_path(job_id))
      plan_found = self._wait_for_plan(plan_path, max_attempts=3, wait_seconds=20)

      if not plan_found:
        raise FileNotFoundError(f"Plan file not found after waiting: {plan_path}")

      actions = self._parser.parse_file(str(plan_path), datetime.now())
      self._scheduler.schedule_many(actions)

      execution_time = execution_result.get("execution_time", time.time() - start_time)
      
      self._filesystem.archive_job(job_id, "success", execution_time)

      return {
        "job_id": job_id,
        "status": "completed",
        "scheduled_actions_count": len(actions),
        **execution_result
      }
    
    except Exception as e:
      elapsed = time.time() - start_time
      self._filesystem.archive_job(job_id, "error", elapsed)
      raise Exception(f"Job {job_id} failed: {str(e)}")

  def _wait_for_plan(self, plan_path: Path, max_attempts: int, wait_seconds: int) -> bool:
    for attempt in range(1, max_attempts + 1):
      print(f"[INFO] Attempt {attempt}: Checking for plan file...")

      if plan_path.exists() and plan_path.stat().st_size > 0:
        print(f"[INFO] Plan file found!")
        return True
      
      if attempt < max_attempts:
        time.sleep(wait_seconds)
        
    return False
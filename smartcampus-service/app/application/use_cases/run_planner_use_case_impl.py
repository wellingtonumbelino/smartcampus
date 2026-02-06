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

    try:
      problem_pddl = self._generate_pddl.execute(input_data)
      
      self._filesystem.setup_job(job_id)
      self._filesystem.write_domain(job_id)
      self._filesystem.write_problem(job_id, problem_pddl)

      execution_result = self._planner.run(job_id)

      if execution_result["success"]:
        plan_path = self._filesystem.get_plan_path(job_id)

        with open(plan_path, "r") as f:
          plan_content = f.read()

        from datetime import datetime
        actions = self._parser.parse_file(plan_content, datetime.now())
        self._scheduler.schedule_many(actions)

        execution_result["scheduled_actions_count"] = len(actions)

      self._filesystem.archive_job(
        job_id,
        "success" if execution_result["success"] else "failed",
        execution_result["execution_time"]
      )

      return {
        "job_id": job_id,
        "status": "completed",
        **execution_result
      }
    
    except Exception as e:
      self._filesystem.archive_job(job_id, "error", 0)
      raise
    
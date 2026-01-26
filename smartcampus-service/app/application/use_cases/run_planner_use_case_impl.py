from app.application.use_cases.run_planner_use_case import RunPlannerUseCase
from app.application.use_cases.generate_pddl_use_case import GeneratePDDLUseCase
from app.infrastructure.pddl.pddl_filesystem_service import PDDLFilesystemService
from app.infrastructure.planner.docker_planner_execution_service import DockerPlannerExecutionService

class RunPlannerUseCaseImpl(RunPlannerUseCase):
  def __init__(self, generate_pddl_use_case: GeneratePDDLUseCase, filesystem_service: PDDLFilesystemService, planner_service: DockerPlannerExecutionService):
    self._generate_pddl = generate_pddl_use_case
    self._filesystem = filesystem_service
    self._planner = planner_service

  def execute(self, input_data) -> dict:
    job_id = self._planner.create_job()

    try:
      problem_pddl = self._generate_pddl.execute(input_data)
      
      self._filesystem.setup_job(job_id)
      self._filesystem.write_domain(job_id)
      self._filesystem.write_problem(job_id, problem_pddl)

      execution_result = self._planner.run(job_id)

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
    
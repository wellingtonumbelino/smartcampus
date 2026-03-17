from fastapi import APIRouter, HTTPException, Depends
from app.infrastructure.planner.planner_output_service import PlannerOutputService
from app.application.use_cases.run_planner_use_case import RunPlannerUseCase
from app.interfaces.http.schemas.environment_request import EnvironmentRequest
from app.interfaces.http.mappers.environment_mapper import map_environment_request_to_dto
from app.interfaces.http.dependencies import get_run_planner_use_case
from app.infrastructure.pddl.pddl_generator_v21 import PDDLGeneratorFromDefinition
from app.application.dto.environment_input_dto import ProblemDefinitionDTO, EnvironmentInputDTO
from app.infrastructure.pddl.pddl_filesystem_service import PDDLFilesystemService
from app.infrastructure.pddl.plan_parser import PDDLPlanParser
from app.interfaces.http.dependencies import get_plan_parser
from typing import Dict, Any
from datetime import datetime

router = APIRouter(prefix="/planner", tags=["Planner"])

# Endpoint existente (compatibilidade)
@router.post("/run")
def run_planner(
  request: EnvironmentRequest,
  use_case: RunPlannerUseCase = Depends(get_run_planner_use_case)
):
  try:
    input_dto = map_environment_request_to_dto(request)

    if isinstance(input_dto, ProblemDefinitionDTO):
      return _run_planner_from_definition(input_dto, use_case)
    else:
      return _run_planner_from_environment(input_dto, use_case)

  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))

def _run_planner_from_definition(
  problem_def_dto: ProblemDefinitionDTO,
  use_case: RunPlannerUseCase
) -> dict:
  try:
    definition_dict = {
      "name": problem_def_dto.name,
      "domain": problem_def_dto.domain,
      "objects": {
        "rooms": problem_def_dto.objects.rooms,
        "air_conditioners": problem_def_dto.objects.air_conditioners,
        "lights": problem_def_dto.objects.lights,
      },
      "init": {
        "fluents": problem_def_dto.init.fluents,
        "timed_events": [
          {
            "time": event.time,
            "type": event.type,
            "predicate": event.predicate,
            "fluent": event.fluent,
            "args": event.args,
            "value": event.value
          }
          for event in problem_def_dto.init.timed_events
        ]
      },
      "goal": {
        "predicates": [
          {
            "predicate": pred.predicate,
            "args": pred.args
          }
          for pred in problem_def_dto.goal.predicates
        ]
      },
      "metric": problem_def_dto.metric
    }

    generator = PDDLGeneratorFromDefinition()
    problem_pddl = generator.generate_from_dict(definition_dict)

    filesystem = PDDLFilesystemService()
    job_id = use_case._planner.create_job()

    filesystem.setup_job(job_id)
    filesystem.write_domain(job_id)
    filesystem.write_problem(job_id, problem_pddl)

    execution_result = use_case._planner.run(job_id)

    if execution_result["success"]:
      plan_path = filesystem.get_plan_path(job_id)

      if not plan_path.exists():
        raise FileNotFoundError(
          f"Plan file not create by planner. "
          f"Check Docker output: {plan_path}"
        )
      
      with open(plan_path, "r") as f:
        plan_content = f.read()

      actions = []

      execution_result["scheduled_actions_count"] = len(actions)
  
    filesystem.archive_job(
      job_id,
      "sucess" if execution_result["success"] else "failure",
      execution_result["execution_time"]
    )

    return {
      "job_id": job_id,
      "status": "completed",
      **execution_result
    }
  
  except Exception as e:
    raise HTTPException(status_code=400, detail=f"Error running planner: {str(e)}")

def _run_planner_from_environment(
    environment_dto: EnvironmentInputDTO,
    use_case: RunPlannerUseCase
  ) -> dict:
  try:
    result = use_case.execute(environment_dto)
    return result
  except Exception as e:
    raise HTTPException(status_code=400, detail=f"Erro ao executar planejador: {str(e)}")

@router.get("/result/{job_id}")
def get_plan(job_id: str):
  """Recupera o resultado de um planejamento executado."""
  output_service = PlannerOutputService(job_id)

  if not output_service.is_ready():
    return {
      "job_id": job_id,
      "status": "not_found",
      "message": "Job not found in history. Check if it has completed.",
      "plan": None
    }
  
  try:
    metadata = output_service.get_metadata()
    plan = output_service.read_plan()
    error_log = output_service.get_error_log()
  except FileNotFoundError as e:
    raise HTTPException(status_code=404, detail=str(e))

  return {
    "job_id": job_id,
    "status": metadata.get("status"),
    "execution_time": metadata.get("execution_time"),
    "timestamp": metadata.get("timestamp"),
    "plan": plan,
    "error": error_log
  }


@router.get("/history")
def list_jobs():
  """Lista todos os planejamentos executados."""
  from app.infrastructure.pddl.pddl_filesystem_service import PDDLFilesystemService

  filesystem_service = PDDLFilesystemService()
  jobs = filesystem_service.list_jobs()

  return {
    "total": len(jobs),
    "jobs": jobs
  }
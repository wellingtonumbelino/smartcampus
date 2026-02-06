from app.application.use_cases.generate_pddl_use_case_impl import GeneratePDDLUseCaseImpl
from app.infrastructure.pddl.pddl_generator_v21 import PDDLGenerator
from app.application.use_cases.run_planner_use_case_impl import RunPlannerUseCaseImpl
from app.infrastructure.pddl.pddl_filesystem_service import PDDLFilesystemService
from app.infrastructure.planner.docker_planner_execution_service import DockerPlannerExecutionService
from app.infrastructure.scheduler.apscheduler_impl import APSchedulerImpl
from app.domain.interfaces.plan_parser import PDDLPlanParser

_scheduler_instance = APSchedulerImpl()
_parser_instance = PDDLPlanParser(time_unit_to_hours=10.0)

def get_generate_pddl_use_case():
  return GeneratePDDLUseCaseImpl(pddl_generator=PDDLGenerator())

def get_run_planner_use_case():
  generate_pddl = get_generate_pddl_use_case()
  filesystem = PDDLFilesystemService()
  planner = DockerPlannerExecutionService()

  return RunPlannerUseCaseImpl(
    generate_pddl_use_case=generate_pddl,
    filesystem_service=filesystem,
    planner_service=planner,
    parser=_parser_instance,
    scheduler=_scheduler_instance
  )
from app.application.use_cases.generate_pddl_use_case_impl import GeneratePDDLUseCaseImpl
from app.infrastructure.pddl.pddl_generator_v21 import PDDLGenerator

def get_generate_pddl_use_case():
  return GeneratePDDLUseCaseImpl(pddl_generator=PDDLGenerator())
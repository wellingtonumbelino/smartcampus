from app.domain.interfaces.pddl_generator import PDDLGenerator
from app.domain.entities.environment import Environment

class FakePDDLGenerator(PDDLGenerator):
  def generate(self, environment: Environment) -> str:
    return "(define (problem fake-problem) (:domain fake-domain))"
from abc import ABC, abstractmethod
from app.domain.entities.environment import Environment

class PDDLGenerator(ABC):
  @abstractmethod
  def generate(self, environment: Environment) -> str:
    """
    Gera a representação PDDL a partir do ambiente de domínio.

    :param environment: Aggregate Root no domíno
    :return: Conteúdo PDDL em formato texto
    """
from abc import ABC, abstractmethod
from app.domain.entities.plan import ScheduleAction

class IScheduler(ABC):
  @abstractmethod
  def schedule_action(self, action: ScheduleAction):
    """Schedule a single action for future execution"""
    pass

  @abstractmethod
  def schedule_many(self, actions: list[ScheduleAction]):
    """Schedule a list of actions"""
    pass
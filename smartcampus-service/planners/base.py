from abc import ABC, abstractmethod
from pathlib import Path

class PlannerResult:
    def __init__(self, raw_plan: str):
        self.raw_plan = raw_plan

class BasePlanner(ABC):
    @abstractmethod
    def run(self, domain: Path, problem: Path) -> PlannerResult:
        pass
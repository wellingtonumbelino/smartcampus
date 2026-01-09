from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tempfile import TemporaryDirectory
from pathlib import Path

from planners.mock import MockPlanner
from parsers.pddl_plan_parser import parse_pddl_plan

app = FastAPI()

class PlanningRequest(BaseModel):
    domain: str
    problem: str
    planner: str = "mock"
    options: dict = {}

@app.post("/plan")
def plan(request: PlanningRequest):
    with TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        domain_file = "app/domain/domain.pddl"
        problem_file = temp_path / "problem.pddl"

        domain_file.write_text(request.domain)
        problem_file.write_text(request.problem)

        planner = MockPlanner()
        result = planner.run(domain_file, problem_file)

        plan = parse_pddl_plan(result.raw_plan)

        return {
            "status": "success",
            "plan": plan,
            "raw_plan": result.raw_plan
        }
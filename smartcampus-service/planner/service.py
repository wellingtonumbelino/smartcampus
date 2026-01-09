from planner.problem_generator import generate_problem_file
from planner.executor import run_planner
from parsers.pddl_plan_parser import parse_pddl_plan

def plan(state):
  problem_path = generate_problem_file(state)
  raw_result = run_planner(problem_path)
  return parse_pddl_plan(raw_result)
import subprocess

from settings import DOMAIN_DIR

def run_planner(problem_file):
  result = subprocess.run(
    [
      "fast-downward.py",
      str(DOMAIN_DIR),
      str(problem_file),
      "--search",
      "astar(lmcut())"
    ],
    capture_output=True,
    text=True
  )

  return result
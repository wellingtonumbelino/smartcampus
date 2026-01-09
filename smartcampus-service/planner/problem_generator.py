from pathlib import Path
from settings import TMP_DIR

def generate_problem_file(state) -> Path:
    TMP_DIR.mkdir(exist_ok=True)
    problem_file = TMP_DIR / "problem.pddl"
    
    pddl_content = build_problem_from_state(state)

    with open(problem_file, "w", encoding="utf-8") as f:
        f.write(pddl_content)

    return problem_file

def build_problem_from_state(state: dict) -> str:
    room = state["room"]
    
    return f"""
      (define (problem smart_campus_problem)
        (:domain smart_campus)

        (:objects
          {room} - room
        )

        (:init

        )

        (:goal
          (and
            (ac-on {room})
          )
        )
    """.strip()

# room = state["room"]
#     people = state["people"]
#     ac_on = state["ac_on"]

#     init_facts = [
#         f"(room {room})",
#         f"(= (people-count {room}) {people})"
#     ]

#     if ac_on:
#         init_facts.append(f"(ac-on {room})")

#     init_block = "\n        ".join(init_facts)
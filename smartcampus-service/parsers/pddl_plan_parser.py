import re

def parse_pddl_plan(raw_plan: str):
    steps = []
    for line in raw_plan.strip().splitlines():
        match = re.match(r"\(([^ ]+)(.*?)\)", line)
        if not match:
            continue
        
        action = match.group(1)
        params = match.group(2).strip().split()

        steps.append({
            "action": action,
            "parameters": params,
            "start": None,
            "duration": None
        })

    return steps
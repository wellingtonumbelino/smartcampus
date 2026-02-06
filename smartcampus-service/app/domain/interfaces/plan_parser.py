import re
from datetime import datetime, timedelta
from app.domain.entities.plan import ScheduleAction

class PDDLPlanParser:
  def __init__(self, time_unit_to_hours: float = 10.0):
    self.time_multiplier = time_unit_to_hours
    self.pattern = r"(\d+\.\d+):\s*\(\s*(\w+)\s+(.*?)\)\s*\[(\d+\.\d+)\]"
    self.action_map = {
      "turn_on_light_during_class": "ON",
      "turn_off_light_when_occupancy_zero": "OFF",
      "turn_on_air_conditioner_during_class": "ON",
      "turn_off_air_conditioner_when_occupancy_zero": "OFF",
      "start_campus_operating": "START"
    }

  def parse_file(self, file_content: str, reference_date: datetime) -> list[ScheduleAction]:
    actions = []

    for line in file_content.splitlines():
      match = re.search(self.pattern, line)

      if not match:
        continue

      raw_time = float(match.group(1))
      action_name = match.group(2)
      params = match.group(3).strip().split()
      duration = float(match.group(4))

      device_id = params[-1] if params else None
      
      command = self.action_map.get(action_name, "UNKNOWN")

      execution_time = reference_date + timedelta(hours=raw_time * self.time_multiplier)

      actions.append(ScheduleAction(
        execution_time=execution_time,
        action_name=action_name,
        target_device_id=device_id,
        command=command,
        duration=duration
      ))

    return actions
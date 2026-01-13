from typing import List
from app.domain.entities.environment import Environment
from app.domain.interfaces.pddl_generator import PDDLGenerator

class PDDLGenerator(PDDLGenerator):
  def generate(self, environment: Environment) -> str:
    lines: List[str] = []

    problem_name = "smart_campus_problem_day_plan"

    lines.append(f"(define (problem {problem_name})")
    lines.append("  (:domain smart_campus)")
    lines.append("")
    lines.append(f"(:requirements :strips :typing :fluents :durative-actions :negative-preconditions :timed-initial-literals)")
    lines.append("")
    lines.append(self._generate_objects(environment))
    lines.append("")
    lines.append(self._generate_init(environment))
    lines.append("")
    lines.append(self._generate_goal(environment))
    lines.append(")")

    return "\n".join(lines)

  def _generate_objects(self, environment: Environment) -> str:
    rooms: list[str] = []
    devices_by_type: dict[str, list[str]] = {}

    for room in environment.rooms:
      rooms.append(self._sanitize_name(room.name))

      for device in room.devices:
        device_type = device.device_type
        device_id = self._sanitize_name(device.id)

        devices_by_type.setdefault(device_type, []).append(device_id)

    lines = [
      "  (:objects",
      f"    {' '.join(sorted(set(rooms)))} - room",
    ]

    for device_type, device_ids in devices_by_type.items():
      unique_devices = sorted(set(device_ids))
      lines.append(f"    {' '.join(unique_devices)} - {device_type}")

    lines.append("   )")

    return "\n".join(lines)

  def _generate_init(self, environment: Environment) -> str:
    fluents = []

    for room in environment.rooms:
      room_name = self._sanitize_name(room.name)
      fluents.append(f"(= (occupancy {room_name}) {room.occupancy})")
    
    lines = [
      "  (:init",
      *fluents,
      "",
      f"  (at 0.1 (operating_hour))",
      f"  (at 0.6 (not (operating_hour)))",
      "   )"
    ]

    return "\n".join(lines)
  
  def _generate_goal(self, environment: Environment) -> str:
    lines = [
      "  (:goal (and",
      "    (not (operating_hour))",
      "  ))"
    ]

    return "\n".join(lines)
  
  @staticmethod
  def _sanitize_name(name: str) -> str:
    return name.lower().replace(" ", "_")
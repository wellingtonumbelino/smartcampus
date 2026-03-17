from typing import List, Dict, Any
from app.domain.interfaces.pddl_generator import PDDLGenerator as IPDDLGenerator
from app.domain.entities.environment import Environment


# =====================================================================
# CLASSE PRINCIPAL: Gera PDDL a partir de EnvironmentInputDTO / Environment
# Mantém compatibilidade com GeneratePDDLUseCaseImpl
# =====================================================================

class PDDLGenerator(IPDDLGenerator):
  """
  Gera PDDL a partir da estrutura Environment (EnvironmentInputDTO convertido).
  
  Esta classe é utilizada pelo GeneratePDDLUseCaseImpl para gerar PDDL
  a partir da estrutura tradicional de rooms e devices.
  """
  
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

    lines.append("  )")

    return "\n".join(lines)

  def _generate_init(self, environment: Environment) -> str:
    lines = ["  (:init"]
    lines.append("    (= (work_time_duration) 0)")
    lines.append("")

    for room in environment.rooms:
      room_name = self._sanitize_name(room.name)
      lines.append(f"    (at 0.2 (people_in_room {room_name}))")
      lines.append("")
      lines.append(f"    (at 0.4 (not (people_in_room {room_name})))")
      lines.append("")

    lines.append("  )")

    return "\n".join(lines)
  
  def _generate_goal(self, environment: Environment) -> str:
    lines = ["  (:goal (and"]

    for room in environment.rooms:
      room_name = self._sanitize_name(room.name)

      for device in room.devices:
        device_id = self._sanitize_name(device.id)
        device_type = device.device_type

        if device_type == "air_conditioner":
          lines.append(f"    (end_class_air {room_name} {device_id})")
        elif device_type == "light":
          lines.append(f"    (end_class_light {room_name} {device_id})")

    lines.append("      (finish_class_time))")
    lines.append("  )")
    
    return "\n".join(lines)
  
  @staticmethod
  def _sanitize_name(name: str) -> str:
    """Remove espaços e converte para minúsculas"""
    return name.lower().replace(" ", "_")

class PDDLGeneratorFromDefinition(IPDDLGenerator):  
  def generate(self, definition_dict: Dict[str, Any]) -> str:
    raise NotImplementedError(
      "Use generate_from_dict(definition_dict) para gerar a partir de dicionário"
    )
  
  def generate_from_dict(self, definition_dict: Dict[str, Any]) -> str:
    """Gera PDDL a partir de uma definição estruturada em dicionário"""
    lines: List[str] = []

    # Problem definition
    lines.append(f"(define (problem {definition_dict['name']})")
    lines.append(f"  (:domain {definition_dict['domain']})")
    lines.append("")

    # Objects
    lines.append(self._generate_objects(definition_dict['objects']))
    lines.append("")

    # Init
    lines.append(self._generate_init(definition_dict['init']))
    lines.append("")

    # Goal
    lines.append(self._generate_goal(definition_dict['goal']))
    lines.append("")

    # Metric (opcional)
    if definition_dict.get('metric'):
      lines.append(f"  (:metric {definition_dict['metric']})")
      lines.append("")
    
    lines.append(")")

    return "\n".join(lines)

  def _generate_objects(self, objects: Dict[str, List[str]]) -> str:
    """Gera a seção (:objects ...) do PDDL"""
    lines = ["  (:objects"]

    if objects.get('rooms'):
      lines.append(f"    {' '.join(objects['rooms'])} - room")

    if objects.get('air_conditioners'):
      lines.append(f"    {' '.join(objects['air_conditioners'])} - air_conditioner")

    if objects.get('lights'):
      lines.append(f"    {' '.join(objects['lights'])} - light")

    lines.append("  )")

    return "\n".join(lines)

  def _generate_init(self, init_data: Dict[str, Any]) -> str:
    """Gera a seção (:init ...) do PDDL com fluents e eventos temporais"""
    lines = ["  (:init"]

    # Fluents iniciais
    fluents = init_data.get('fluents', {})
    for fluent_name, fluent_values in fluents.items():
      if isinstance(fluent_values, dict):
        # Fluents com argumentos: (= (people_in_room bl1_sl1) 0)
        for args_key, value in fluent_values.items():
          lines.append(f"    (= ({fluent_name} {args_key}) {value})")
      else:
        # Fluents simples: (= (metric_total_cost) 0)
        lines.append(f"    (= ({fluent_name}) {fluent_values})")

    lines.append("")

    # Eventos temporais
    timed_events = init_data.get('timed_events', [])
    for event in timed_events:
      time = event['time']

      if event['type'] == "predicate":
        # Predicado temporal: (at 0.0 (operating_hour))
        predicate = event['predicate']
        lines.append(f"    (at {time} ({predicate}))")

      elif event['type'] == "fluent":
        # Fluent temporal: (at 1.0 (= (people_in_room bl1_sl1) 8))
        fluent_name = event['fluent']
        args = " ".join(event.get('args', []))
        value = event['value']

        if args:
          lines.append(f"    (at {time} (= ({fluent_name} {args}) {value}))")
        else:
          lines.append(f"    (at {time} (= ({fluent_name}) {value}))")
      
    lines.append("  )")

    return "\n".join(lines)
  
  def _generate_goal(self, goal_data: Dict[str, Any]) -> str:
    """Gera a seção (:goal ...) do PDDL"""
    lines = ["  (:goal"]
    lines.append("    (and")

    predicates = goal_data.get('predicates', [])
    for pred in predicates:
      predicate_name = pred['predicate']
      args = pred.get('args', [])

      if args:
        args_str = " ".join(args)
        lines.append(f"      ({predicate_name} {args_str})")
      else:
        lines.append(f"      ({predicate_name})")
      
    lines.append("    )")
    lines.append("  )")

    return "\n".join(lines)
  
  @staticmethod
  def _sanitize_name(name: str) -> str:
    """Remove espaços e converte para minúsculas"""
    return name.lower().replace(" ", "_")
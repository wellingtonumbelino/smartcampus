from app.interfaces.http.schemas.environment_request import (
  EnvironmentRequest
)
from app.application.dto.environment_input_dto import (
  EnvironmentInputDTO,
  RoomInputDTO,
  DeviceInputDTO,
  ProblemDefinitionDTO,
  TimedEventDTO,
  InitDTO,
  GoalDTO,
  GoalPredicateDTO,
  ObjectsDTO
)

def map_environment_request_to_dto(request: EnvironmentRequest) -> EnvironmentInputDTO | ProblemDefinitionDTO:
  if request.rooms:
    return EnvironmentInputDTO(
      name=request.name,
      rooms=[
        RoomInputDTO(
          name=room.name,
          type=room.type,
          occupancy=room.occupancy,
          devices=[
            DeviceInputDTO(
              id=device.id,
              type=device.type
            )
            for device in room.devices
          ]
        )
        for room in request.rooms
      ]
    )

  if request.problem_definition:
    problem_def = request.problem_definition

    timed_events = [
      TimedEventDTO(
        time=event.time,
        type=event.type,
        predicate=event.predicate,
        fluent=event.fluent,
        args=event.args,
        value=event.value
      )
      for event in problem_def.init.timed_events
    ]

    init_dto = InitDTO(
      fluents=problem_def.init.fluents,
      timed_events=timed_events
    )

    goal_predicates = [
      GoalPredicateDTO(
        predicate=pred.predicate,
        args=pred.args
      )
      for pred in problem_def.goal.predicates
    ]

    goal_dto = GoalDTO(predicates=goal_predicates)

    objects_dto = ObjectsDTO(
      rooms=problem_def.objects.rooms,
      air_conditioners=problem_def.objects.air_conditioners,
      lights=problem_def.objects.lights
    )

    return ProblemDefinitionDTO(
      name=problem_def.name,
      domain=problem_def.domain,
      objects=objects_dto,
      init=init_dto,
      goal=goal_dto,
      metric=problem_def.metric
    )
  
  raise ValueError("Invalid environment request: missing rooms or problem definition")

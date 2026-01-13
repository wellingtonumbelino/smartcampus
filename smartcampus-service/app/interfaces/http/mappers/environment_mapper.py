from app.interfaces.http.schemas.environment_request import EnvironmentRequest
from app.application.dto.environment_input_dto import (
  EnvironmentInputDTO,
  RoomInputDTO,
  DeviceInputDTO
)

def map_environment_request_to_dto(request: EnvironmentRequest) -> EnvironmentInputDTO:
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
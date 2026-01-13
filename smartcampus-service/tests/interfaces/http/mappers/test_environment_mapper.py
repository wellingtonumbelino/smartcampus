from app.interfaces.http.schemas.environment_request import EnvironmentRequest
from app.interfaces.http.mappers.environment_mapper import map_environment_request_to_dto

def test_environment_request_to_dto_mapper():
  request = EnvironmentRequest(
    name="bl1",
    rooms=[
      {
        "name": "sl1",
        "type": "room",
        "occupancy": 5,
        "devices": [
          {
            "id": "ac1",
            "type": "air_conditioner"
          }
        ]
      }
    ]
  )

  dto = map_environment_request_to_dto(request)

  assert dto.name == "bl1"
  assert dto.rooms[0].devices[0].type == "air_conditioner"
from app.interfaces.http.schemas.environment_request import EnvironmentRequest

def test_environment_request_schema():
  data = {
    "name": "bl1",
    "rooms": [
      {
        "name": "sl1",
        "type": "room",
        "occupancy": 5,
        "devices": [
          {"id": "ac1", "type": "air_conditioner"},
          {"id": "l1", "type": "light"}
        ]
      }
    ]
  }

  env = EnvironmentRequest(**data)

  assert env.name == "bl1"
  assert env.rooms[0].devices[0].id == "ac1"
  assert env.rooms[0].devices[1].type == "light"
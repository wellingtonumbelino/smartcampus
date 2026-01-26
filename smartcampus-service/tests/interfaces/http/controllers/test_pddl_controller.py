from fastapi.testclient import TestClient
from app.main import app
from app.interfaces.http.dependencies import get_generate_pddl_use_case
from tests.interfaces.http.fakes.fake_use_case import FakeGeneratePDDLUseCase

client = TestClient(app)

def override_use_case():
  return FakeGeneratePDDLUseCase()

app.dependency_overrides[get_generate_pddl_use_case] = override_use_case

def test_generate_pddl_endpoint():
  payload = {
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

  response = client.post("/pddl", json=payload)

  assert response.status_code == 200
  assert response.json() == "FAKE_PDDL_FROM_API"
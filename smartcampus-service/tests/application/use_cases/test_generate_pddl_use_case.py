from app.application.use_cases.generate_pddl_use_case_impl import GeneratePDDLUseCaseImpl
from app.application.dto.environment_input_dto import (
  EnvironmentInputDTO,
  RoomInputDTO,
  DeviceInputDTO
)
from tests.application.fakes.fake_pddl_generator import FakePDDLGenerator

def test_generate_pddl_use_case_happy_path():
  fake_generator = FakePDDLGenerator()
  use_case = GeneratePDDLUseCaseImpl(fake_generator)

  input_dto = EnvironmentInputDTO(
    name="bl1",
    rooms=[
      RoomInputDTO(
        name="sl1",
        type="room",
        occupancy=5,
        devices=[
          DeviceInputDTO(id="ac1", type="air_conditioner"),
          DeviceInputDTO(id="l1", type="light")
        ]
      )
    ]
  )

  result = use_case.execute(input_dto)

  assert result == "FAKE_PDDL_OUTPUT"
  assert fake_generator.called_with.name == "bl1"
  assert fake_generator.called_with.rooms[0].devices[0].id == "ac1"
  assert fake_generator.called_with.rooms[0].devices[1].device_type == "light"
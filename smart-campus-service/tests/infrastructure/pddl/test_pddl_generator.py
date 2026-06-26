from app.domain.entities.air_conditioner import AirConditioner
from app.domain.entities.light import Light
from app.domain.entities.room import Room
from app.domain.entities.environment import Environment
from app.infrastructure.pddl.pddl_generator_v21 import PDDLGenerator

def test_generate_pddl_for_simple_enviroment():
  ac1 = AirConditioner("ac1")
  l1 = Light("l1")
  l2 = Light("l2")

  room = Room(name="sl1", type="room", occupancy=5, devices=[ac1, l1, l2])
  environment = Environment(name="bl1", rooms=[room])

  generator = PDDLGenerator()
  pddl = generator.generate(environment)

  assert "(define (problem smart_campus_problem_day_plan)" in pddl
  assert "(= (work_time_duration) 0)" in pddl
  assert "(at 0.1 (operating_hour))" in pddl
  assert "(at 0.2 (people_in_room sl1))" in pddl
  assert "(at 0.4 (not (people_in_room sl1)))" in pddl
  assert "(end_class_air sl1 ac1)" in pddl
  assert "(end_class_light sl1 l1)" in pddl
  assert "(finish_class_time)" in pddl
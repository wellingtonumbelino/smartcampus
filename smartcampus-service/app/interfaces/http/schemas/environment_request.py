from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class TimedEventRequest(BaseModel):
  time: float
  type: str # "predicate" or "fluent"
  predicate: Optional[str] = None
  fluent: Optional[str] = None
  args: Optional[List[str]] = None
  value: Optional[int] = None

class InitRequest(BaseModel):
  fluents: Dict[str, Dict[str, Any]]
  timed_events: List[TimedEventRequest]

class GoalPredicateRequest(BaseModel):
  predicate: str
  args: Optional[List[str]] = None

class GoalRequest(BaseModel):
  predicates: List[GoalPredicateRequest]

class ObjectsRequest(BaseModel):
  rooms: List[str]
  air_conditioners: List[str]
  lights: List[str]

class ProblemDefinitionRequest(BaseModel):
  name: str
  domain: str
  objects: ObjectsRequest
  init: InitRequest
  goal: GoalRequest
  metric: Optional[str] = None

class DeviceRequest(BaseModel):
  id: str
  type: str

class RoomRequest(BaseModel):
  name: str
  type: str
  occupancy: int
  devices: List[DeviceRequest]

class EnvironmentRequest(BaseModel):
  name: str
  rooms: Optional[List[RoomRequest]] = None
  problem_definition: Optional[ProblemDefinitionRequest] = None
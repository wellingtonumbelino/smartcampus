from pydantic import BaseModel
from typing import List

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
  rooms: List[RoomRequest]
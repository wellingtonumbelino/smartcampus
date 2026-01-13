from dataclasses import dataclass
from typing import List

@dataclass
class DeviceInputDTO:
  id: str
  type: str

@dataclass
class RoomInputDTO:
  name: str
  type: str
  occupancy: int
  devices: List[DeviceInputDTO]

@dataclass
class EnvironmentInputDTO:
  name: str
  rooms: List[RoomInputDTO]
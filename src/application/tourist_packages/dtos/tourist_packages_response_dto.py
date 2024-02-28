from dataclasses import dataclass
from datetime import datetime


@dataclass
class TouristPackagesResponseDto:
    id: str
    name: str
    description: str
    destination_place: str
    duration: int
    max_capacity: int
    cost: float
    start_date: datetime
    end_date: datetime
    image: str
    admin_id: str


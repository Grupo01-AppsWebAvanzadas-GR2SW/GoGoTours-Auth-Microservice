from dataclasses import dataclass
import datetime


@dataclass
class ReservesResponseDto:
    id: str
    id_tourist_package: str
    id_customer: str
    date_sent: datetime

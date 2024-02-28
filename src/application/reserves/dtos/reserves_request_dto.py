from dataclasses import dataclass


@dataclass
class ReservesRequestDto:
    id_tourist_package: str
    id_customer: str

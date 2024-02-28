from abc import ABC, abstractmethod
from src.application.reserves.dtos.reserves_response_dto import ReservesResponseDto
from src.application.reserves.dtos.reserves_request_dto import ReservesRequestDto


class ReservesServiceAsync(ABC):
    @abstractmethod
    async def get_reserves(self) -> list[ReservesResponseDto]:
        pass

    @abstractmethod
    async def create_reserve(self, reserve: ReservesRequestDto):
        pass

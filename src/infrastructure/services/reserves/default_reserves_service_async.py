from datetime import datetime
from src.domain.reserves.entities.reserve import Reserve
from src.application.reserves.services.reserve_service_async import ReservesServiceAsync
from src.application.reserves.dtos.reserves_request_dto import ReservesRequestDto
from src.application.reserves.dtos.reserves_response_dto import ReservesResponseDto
from src.application.reserves.repositories.reserve_repository_async import ReservesRepositoryAsync
from injector import inject


class DefaultReservesSeviceAsync(ReservesServiceAsync):
    @inject
    def __init__(self, reserve_repository_async: ReservesRepositoryAsync):
        self._reserve_repository_async = reserve_repository_async

    async def get_reserves(self) -> list[ReservesResponseDto]:
        reserves = await self._reserve_repository_async.list_async()
        return [ReservesResponseDto(
            id=reserve.id,
            id_tourist_package=reserve.id_tourist_package,
            id_customer=reserve.id_customer,
            date_sent=reserve.date_sent
        ) for reserve in reserves]

    async def create_reserve(self, reserve: ReservesRequestDto):
        await self._reserve_repository_async.add_async(Reserve(id_tourist_package=reserve.id_tourist_package,
                                                               id_customer=reserve.id_customer))

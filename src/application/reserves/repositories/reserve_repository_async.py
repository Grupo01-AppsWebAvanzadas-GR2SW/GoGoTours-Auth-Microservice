from abc import ABC, abstractmethod
from src.domain.reserves.entities.reserve import Reserve
from src.application.common.repositories.generic_repository_async import GenericRepositoryAsync


class ReservesRepositoryAsync(GenericRepositoryAsync[Reserve, str], ABC):
    @abstractmethod
    async def list_async(self) -> list[Reserve]:
        pass

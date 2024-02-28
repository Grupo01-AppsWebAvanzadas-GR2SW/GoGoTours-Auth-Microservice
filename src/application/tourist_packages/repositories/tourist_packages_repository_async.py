from abc import ABC, abstractmethod
from src.domain.tourist_packages.entities.tourist_package import TouristPackage
from src.application.common.repositories.generic_repository_async import GenericRepositoryAsync


class TouristPackagesRepositoryAsync(GenericRepositoryAsync[TouristPackage, str], ABC):
    @abstractmethod
    async def get_n_latest_packages(self, n: int) -> list[TouristPackage]:
        pass

    @abstractmethod
    async def list_async(self) -> list[TouristPackage]:
        pass

    @abstractmethod
    async def get_packages_by_start_date(self, start_date: str) -> list[TouristPackage]:
        pass

    @abstractmethod
    async def get_by_name_async(self, name: str) -> TouristPackage:
        pass

    @abstractmethod
    async def get_by_id_async(self, id: str) -> TouristPackage:
        pass




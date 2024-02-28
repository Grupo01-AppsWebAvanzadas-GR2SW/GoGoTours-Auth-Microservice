from abc import ABC, abstractmethod
from src.application.tourist_packages.dtos.tourist_packages_response_dto import TouristPackagesResponseDto


class TouristPackagesServiceAsync(ABC):
    @abstractmethod
    async def get_tourist_packages(self) -> list[TouristPackagesResponseDto]:
        pass

    @abstractmethod
    async def get_tourist_package_by_name(self, name: str) -> TouristPackagesResponseDto:
        pass

    @abstractmethod
    async def get_tourist_packages_by_id(self, id: str) -> TouristPackagesResponseDto:
        pass

    @abstractmethod
    async def add_package(self, tourist_package: TouristPackagesResponseDto):
        pass

    @abstractmethod
    async def edit_package(self, tourist_package: TouristPackagesResponseDto):
        pass

    @abstractmethod
    async def delete_package(self, name: str):
        pass

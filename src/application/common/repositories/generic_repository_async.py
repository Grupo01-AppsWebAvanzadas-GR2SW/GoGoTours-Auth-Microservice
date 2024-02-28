from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional
from src.domain.common.entities.base_entity import BaseEntity


ID = TypeVar("ID")
T = TypeVar("T", bound=BaseEntity)


class GenericRepositoryAsync(ABC, Generic[T, ID]):
    @abstractmethod
    async def get_async(self, entity_id: ID) -> Optional[T]:
        pass

    @abstractmethod
    async def list_async(self) -> list[T]:
        pass

    @abstractmethod
    async def add_async(self, item: T) -> None:
        pass

    @abstractmethod
    async def add_many_async(self, items: list[T]) -> None:
        pass

    @abstractmethod
    async def update_async(self, item: T) -> None:
        pass

    @abstractmethod
    async def update_many_async(self, items: list[T]) -> None:
        pass

    @abstractmethod
    async def delete_async(self, item: T) -> None:
        pass

    @abstractmethod
    async def delete_many_async(self, items: list[T]) -> None:
        pass

    @abstractmethod
    async def delete_by_id_async(self, entity_id: ID) -> None:
        pass

    @abstractmethod
    async def exists_async(self, entity_id: ID) -> bool:
        pass

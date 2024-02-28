from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional
from src.domain.common.entities.base_entity import BaseEntity


ID = TypeVar("ID")
T = TypeVar("T", bound=BaseEntity)

class GenericRepository(ABC, Generic[T, ID]):
    @abstractmethod
    def get(self, entity_id: ID) -> Optional[T]:
        pass

    @abstractmethod
    def list(self) -> list[T]:
        pass

    @abstractmethod
    def add(self, item: T) -> None:
        pass

    @abstractmethod
    def add_many(self, items: list[T]) -> None:
        pass

    @abstractmethod
    def update(self, item: T) -> None:
        pass

    @abstractmethod
    def update_many(self, items: list[T]) -> None:
        pass

    @abstractmethod
    def delete(self, item: T) -> None:
        pass

    @abstractmethod
    def delete_many(self, items: list[T]) -> None:
        pass

    @abstractmethod
    def delete_by_id(self, entity_id: ID) -> None:
        pass

    @abstractmethod
    def exists(self, entity_id: ID) -> bool:
        pass

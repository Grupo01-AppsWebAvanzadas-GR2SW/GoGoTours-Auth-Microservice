from typing import Optional, TypeVar, Generic, Any, Dict
from datetime import datetime
from abc import ABC


ID = TypeVar('ID')


class BaseEntity(ABC, Generic[ID]):
    def __init__(self, entity_id: ID):
        self._id: ID = entity_id
        self._created_at: datetime = datetime.now()
        self._updated_at: Optional[datetime] = None

    @property
    def id(self) -> ID:
        return self._id

    @id.setter
    def id(self, entity_id: ID):
        self._id = entity_id

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def set_updated_at_now(self) -> None:
        self._updated_at = datetime.now()

    def merge_dict(self, source: Dict[str, Any]) -> None:
        self._created_at = source["created_at"] if 'created_at' in source else datetime.now()
        self._updated_at = source["updated_at"] if 'updated_at' in source else None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "created_at": self._created_at,
            "updated_at": self._updated_at
        }

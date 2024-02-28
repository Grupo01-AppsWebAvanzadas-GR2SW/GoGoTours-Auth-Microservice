from typing import Dict, Any
from src.domain.common.entities.base_entity import BaseEntity


class Reserve(BaseEntity[str]):

    def __init__(self, id_tourist_package: str = '', id_customer: str = '', entity_id: str = ''):
        super().__init__(entity_id)
        self._id_tourist_package = id_tourist_package
        self._id_customer = id_customer

    @property
    def id_tourist_package(self) -> str:
        return self._id_tourist_package

    @id_tourist_package.setter
    def id_tourist_package(self, value: str):
        if not isinstance(value, str):
            raise TypeError('id_tourist_package must be a string')
        if len(value) < 1 or len(value) > 1024:
            raise ValueError('id_tourist_package must be between 1 and 1024 characters')
        self._id_tourist_package = value

    @property
    def id_customer(self) -> str:
        return self._id_customer

    @id_customer.setter
    def id_customer(self, value: str):
        if not isinstance(value, str):
            raise TypeError('id_customer must be a string')
        if len(value) < 1 or len(value) > 1024:
            raise ValueError('id_customer must be between 1 and 1024 characters')
        self._id_customer = value

    def merge_dict(self, source: Dict[str, Any]) -> None:
        super().merge_dict(source)
        self._id_tourist_package = source["id_tourist_package"] if 'id_tourist_package' in source else ''
        self._id_customer = source["id_customer"] if 'id_customer' in source else ''

    def to_dict(self) -> Dict[str, Any]:
        base_dict = super().to_dict()
        base_dict['id_tourist_package'] = self._id_tourist_package
        base_dict['id_customer'] = self._id_customer
        return base_dict

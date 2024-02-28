from typing import Dict, Any
from src.domain.common.entities.base_entity import BaseEntity


class TouristPackage(BaseEntity[str]):

    def __init__(self, name: str = '', description: str = '', destination_place: str = '', duration: int = 0,
                 max_capacity: int = 0, cost: float = 0, start_date: str = '', end_date: str = '', entity_id: str = '',
                 image: str = '', admin_id: str = ''):
        super().__init__(entity_id)
        self._name = name
        self._description = description
        self._destination_place = destination_place
        self._duration = duration
        self._max_capacity = max_capacity
        self._cost = cost
        self._start_date = start_date
        self._end_date = end_date
        self.image = image
        self.admin_id = admin_id

    @property
    def image(self) -> str:
        return self._image

    @image.setter
    def image(self, value: str):
        if not isinstance(value, str):
            raise TypeError('image url must be a string')
        self._image = value

    @property
    def admin_id(self) -> str:
        return self._admin_id

    @admin_id.setter
    def admin_id(self, value: str):
        if not isinstance(value, str):
            raise TypeError('admin id must be a string')
        self._admin_id = value

    # getter para el nombre
    @property
    def name(self) -> str:
        return self._name

    # setter para el nombre
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError('name must be a string')
        if len(value) < 1 or len(value) > 1024:
            raise ValueError('name must be between 1 and 1024 characters')
        self._name = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        if not isinstance(value, str):
            raise TypeError('description must be a string')
        if len(value) < 1 or len(value) > 1024:
            raise ValueError('description must be between 1 and 1024 characters')
        self._description = value

    @property
    def destination_place(self) -> str:
        return self._destination_place

    @destination_place.setter
    def destination_place(self, value: str):
        if not isinstance(value, str):
            raise TypeError('destination_place must be a string')
        if len(value) < 1 or len(value) > 1024:
            raise ValueError('destination_place must be between 1 and 1024 characters')
        self._destination_place = value

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, value: int):
        if not isinstance(value, int):
            raise TypeError('duration must be an integer')
        if value < 1 or value > 100:
            raise ValueError('duration must be between 1 and 100')
        self._duration = value

    @property
    def max_capacity(self) -> int:
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, value: int):
        if not isinstance(value, int):
            raise TypeError('max_capacity must be an integer')
        if value < 1 or value > 100:
            raise ValueError('max_capacity must be between 1 and 100')
        self._max_capacity = value

    @property
    def cost(self) -> float:
        return self._cost

    @cost.setter
    def cost(self, value: float):
        if not isinstance(value, float):
            raise TypeError('cost must be a float')
        if value < 1 or value > 10000:
            raise ValueError('cost must be between 1 and 10000')
        self._cost = value

    @property
    def start_date(self) -> str:
        return self._start_date

    @start_date.setter
    def start_date(self, value: str):
        if not isinstance(value, str):
            raise TypeError('start_date must be a string')
        if len(value) < 1 or len(value) > 1024:
            raise ValueError('start_date must be between 1 and 1024 characters')
        self._start_date = value

    @property
    def end_date(self) -> str:
        return self._end_date

    @end_date.setter
    def end_date(self, value: str):
        if not isinstance(value, str):
            raise TypeError('end_date must be a string')
        if len(value) < 1 or len(value) > 1024:
            raise ValueError('end_date must be between 1 and 1024 characters')
        self._end_date = value

    def merge_dict(self, source: Dict[str, Any]) -> None:
        super().merge_dict(source)
        self._name = source["name"] if 'name' in source else ''
        self._description = source["description"] if 'description' in source else ''
        self._destination_place = source["destination_place"] if 'destination_place' in source else ''
        self._duration = source["duration"] if 'duration' in source else 0
        self._max_capacity = source["max_capacity"] if 'max_capacity' in source else 0
        self._cost = source["cost"] if 'cost' in source else 0
        self._start_date = source["start_date"] if 'start_date' in source else ''
        self._end_date = source["end_date"] if 'end_date' in source else ''
        self._image = source["image"] if 'image' in source else ''
        self._admin_id = source["admin_id"] if 'admin_id' in source else ''

    def to_dict(self) -> Dict[str, Any]:
        base_dict = super().to_dict()
        base_dict["name"] = self._name
        base_dict["description"] = self._description
        base_dict["destination_place"] = self._destination_place
        base_dict["duration"] = self._duration
        base_dict["max_capacity"] = self._max_capacity
        base_dict["cost"] = self._cost
        base_dict["start_date"] = self._start_date
        base_dict["end_date"] = self._end_date
        base_dict["image"] = self._image
        base_dict["admin_id"] = self._admin_id
        return base_dict

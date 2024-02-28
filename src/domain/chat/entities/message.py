from typing import Dict, Any
from src.domain.common.entities.base_entity import BaseEntity


class Message(BaseEntity[str]):
    def __init__(self, text: str = '', entity_id: str = '', sender_id: str = '', conversation_id: str = ''):
        super().__init__(entity_id)
        self._text: str = text
        self._sender_id: str = sender_id
        self._conversation_id: str = conversation_id

    @property
    def text(self) -> str:
        return self._text

    @property
    def sender_id(self) -> str:
        return self._sender_id

    @property
    def conversation_id(self) -> str:
        return self._conversation_id

    def merge_dict(self, source: Dict[str, Any]) -> None:
        super().merge_dict(source)
        self._text = source["text"] if 'text' in source else ''
        self._sender_id = source["sender_id"] if 'sender_id' in source else ''
        self._conversation_id = source["conversation_id"] if 'conversation_id' in source else ''

    def to_dict(self) -> Dict[str, Any]:
        base_dict = super().to_dict()
        base_dict["text"] = self._text
        base_dict["sender_id"] = self._sender_id
        base_dict["conversation_id"] = self._conversation_id
        return base_dict

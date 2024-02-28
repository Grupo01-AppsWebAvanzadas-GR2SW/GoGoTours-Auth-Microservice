from typing import Dict, Any
from src.domain.common.entities.base_entity import BaseEntity
from src.domain.chat.entities.message import Message


class Conversation(BaseEntity[str]):
    def __init__(self, customer_id: str, admin_id: str, messages: list[Message] = (), entity_id: str = ''):
        super().__init__(entity_id)
        self._participants: list[str] = [customer_id, admin_id]
        self._messages: list[Message] = list(messages)

    @property
    def participants(self) -> list[str]:
        return self._participants

    @property
    def messages(self) -> list[Message]:
        return self._messages

    def merge_dict(self, source: Dict[str, Any]) -> None:
        super().merge_dict(source)
        self._participants = source['participants'] if 'participants' in source else []
        self._messages = []
        for message in source['messages']:
            message_entity = Message()
            message_entity.merge_dict(message)
            self._messages.append(message_entity)

    def to_dict(self) -> Dict[str, Any]:
        base_dict = super().to_dict()
        base_dict['participants'] = self._participants
        base_dict['messages'] = [message.to_dict() for message in self._messages]
        return base_dict

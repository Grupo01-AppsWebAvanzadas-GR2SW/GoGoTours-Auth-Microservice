from dataclasses import dataclass
from src.application.chat.dtos.message_response_dto import MessageResponseDto


@dataclass
class ConversationResponseDto:
    def __init__(
            self,
            conversation_id: str,
            recipient_name: str,
            messages: list[MessageResponseDto]
    ):
        self._conversation_id = conversation_id
        self._recipient_name = recipient_name
        self._messages = messages

    @property
    def conversation_id(self):
        return self._conversation_id

    @property
    def recipient_name(self):
        return self._recipient_name

    @property
    def messages(self):
        return self._messages

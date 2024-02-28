from dataclasses import dataclass
from datetime import datetime

from src.application.utils import format_date_for_chat


@dataclass
class ConversationSummaryResponseDto:
    def __init__(
        self,
        conversation_id: str,
        recipient_name: str,
        last_message: str,
        last_message_date: datetime
    ):
        self._id = conversation_id
        self._recipient_name = recipient_name
        self._last_message = last_message
        self._last_message_date = format_date_for_chat(last_message_date)

    @property
    def id(self):
        return self._id

    @property
    def recipient_name(self):
        return self._recipient_name

    @property
    def last_message(self):
        return self._last_message

    @property
    def last_message_date(self):
        return self._last_message_date

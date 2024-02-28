from dataclasses import dataclass
from datetime import datetime
from src.application.utils import format_date_for_chat


@dataclass
class MessageResponseDto:
    def __init__(self, text: str, date_sent: str | datetime):
        self.text = text
        self.date_sent = date_sent

    @property
    def date_sent(self) -> str:
        return self._date_sent

    @date_sent.setter
    def date_sent(self, value):
        if isinstance(value, str):
            self._date_sent = value
        elif isinstance(value, datetime):
            self._date_sent = format_date_for_chat(value)
        else:
            raise ValueError("The date type is not valid.")
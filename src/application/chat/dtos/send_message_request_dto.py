from dataclasses import dataclass


@dataclass
class SendMessageRequestDto:
    conversation_id: str
    sender_id: str
    message: str

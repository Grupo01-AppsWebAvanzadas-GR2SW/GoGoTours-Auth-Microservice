from dataclasses import dataclass


@dataclass
class ConversationRequestDto:
    sender_id: str
    conversation_id: str

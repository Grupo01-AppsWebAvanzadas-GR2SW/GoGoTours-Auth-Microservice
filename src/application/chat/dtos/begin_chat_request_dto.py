from dataclasses import dataclass


@dataclass
class BeginChatRequestDto:
    customer_id: str
    admin_id: str

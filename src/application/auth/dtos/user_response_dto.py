from dataclasses import dataclass

@dataclass
class UserResponseDto:
    username: str
    id: str
    is_admin: bool

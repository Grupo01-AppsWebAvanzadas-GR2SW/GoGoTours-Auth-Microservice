from dataclasses import dataclass

@dataclass
class UserLoginRequestDto:
    email: str
    password: str
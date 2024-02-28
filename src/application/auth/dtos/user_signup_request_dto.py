from dataclasses import dataclass

@dataclass
class UserSignupRequestDto:
    email: str
    password: str
    username: str

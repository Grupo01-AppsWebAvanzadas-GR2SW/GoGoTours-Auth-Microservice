from dataclasses import dataclass


@dataclass
class RequestResetPasswordRequestDto:
    email: str

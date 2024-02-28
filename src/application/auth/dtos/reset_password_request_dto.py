from dataclasses import dataclass

@dataclass
class ResetPasswordRequestDto:
    reset_token: str
    new_password: str
    email: str
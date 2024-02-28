from abc import ABC, abstractmethod
from src.application.auth.dtos.user_login_request_dto import UserLoginRequestDto
from src.application.auth.dtos.user_signup_request_dto import UserSignupRequestDto
from src.application.auth.dtos.user_response_dto import UserResponseDto
from src.application.auth.dtos.reset_password_request_dto import ResetPasswordRequestDto

class ResetPasswordServiceAsync(ABC):
    @abstractmethod
    async def request_reset_password(self, email: str) -> None:
        pass

    @abstractmethod
    async def reset_password(self, reset_token: str, new_password: str) -> bool:
        pass

    @abstractmethod
    async def check_user_exists(self, email):
        pass

    @abstractmethod
    async def generate_reset_token(self, email):
        pass

    @abstractmethod
    async def send_reset_email(self, email, reset_token):
        pass


from abc import ABC, abstractmethod
from src.application.auth.dtos.user_login_request_dto import UserLoginRequestDto
from src.application.auth.dtos.user_signup_request_dto import UserSignupRequestDto
from src.application.auth.dtos.user_response_dto import UserResponseDto


class SignupServiceAsync(ABC):

    @abstractmethod
    async def signup_user(self, signup_request: UserSignupRequestDto):
        pass
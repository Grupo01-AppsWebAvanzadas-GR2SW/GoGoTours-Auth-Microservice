from abc import ABC, abstractmethod
from typing import Optional

from src.application.auth.dtos.user_login_request_dto import UserLoginRequestDto
from src.application.auth.dtos.user_signup_request_dto import UserSignupRequestDto
from src.application.auth.dtos.user_response_dto import UserResponseDto

class LoginServiceAsync(ABC):

    @abstractmethod
    async def login(self, user: UserLoginRequestDto) -> Optional[UserResponseDto]:
        pass

    @abstractmethod
    async def get_username(self, user_id: str) -> UserResponseDto:
        pass
from fastapi import Depends

from src.domain.auth.entities.user import User
from src.application.auth.services.login_service_async import LoginServiceAsync
from src.application.auth.dtos.user_login_request_dto import UserLoginRequestDto
from src.application.auth.dtos.user_response_dto import UserResponseDto
from src.application.auth.repositories.users_repository_async import UsersRepositoryAsync
from typing import Optional


class DefaultLoginServiceAsync(LoginServiceAsync):
    def __init__(self, users_repository_async: UsersRepositoryAsync = Depends(UsersRepositoryAsync)):
        self._users_repository_async = users_repository_async

    async def get_username(self, user_id: str) -> str:
        user = await self._users_repository_async.get_async(user_id)
        if user:
            return user.username
        else:
            return ''

    async def login(self, user_dto: UserLoginRequestDto) -> Optional[UserResponseDto]:
        user = await self._users_repository_async.get_user_by_email(user_dto.email)
        if user:
            if self._users_repository_async.password_matches(user_dto.password, user.password):
                return UserResponseDto(username=user.username, id=user.id, is_admin=user.is_admin)
            else:
                return None
        else:
            return None

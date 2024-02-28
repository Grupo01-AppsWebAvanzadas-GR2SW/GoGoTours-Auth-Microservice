from abc import ABC, abstractmethod
from typing import Optional
from src.domain.auth.entities.user import User
from src.application.common.repositories.generic_repository_async import GenericRepositoryAsync


class UsersRepositoryAsync(GenericRepositoryAsync[User, str], ABC):

    @abstractmethod
    async def get_user_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    async def password_matches(self, provided_password: str, hashed_password: str) -> bool:
        pass

    @abstractmethod
    async def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    async def update_user(self, user: User) -> Optional[User]:
        pass

    @abstractmethod
    async def get_user_by_reset_token(self, token: str) -> Optional[User]:
        pass

    @abstractmethod
    async def generate_reset_token(self, email):
        pass

    @abstractmethod
    async def check_user_exists(self, email: str) -> bool:
        pass

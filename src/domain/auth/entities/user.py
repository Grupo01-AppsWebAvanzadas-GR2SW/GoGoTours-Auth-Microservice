
from typing import Dict, Any, Optional
from src.domain.common.entities.base_entity import BaseEntity


class User(BaseEntity[str]):
    def __init__(self, email: str = '', entity_id: str = '', password: str = '', username: str = "",
                 is_admin: bool = False, token: Optional[str] = None):
        super().__init__(entity_id)
        self._email = email
        self._password = password
        self._username = username
        self._is_admin = is_admin
        self._token = token

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if not isinstance(value, str):
            raise TypeError('email must be a string')
        if len(value) < 1 or len(value) > 64:
            raise ValueError('email must be between 1 and 64 characters')
        self._email = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str):
        if not isinstance(value, str):
            raise TypeError('password must be a string')
        if len(value) < 8 or len(value) > 64:
            raise ValueError('password must be between 8 and 64 characters')

        self._password = value

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str):
        if not isinstance(value, str):
            raise TypeError('password must be a string')
        if len(value) < 8 or len(value) > 64:
            raise ValueError('password must be between 8 and 64 characters')
        self._username = value

    @property
    def is_admin(self) -> bool:
        return self._is_admin

    @property
    def token(self) -> str:
        return self._email

    @token.setter
    def token(self, value: str):
        self._token = value

    def merge_dict(self, source: Dict[str, Any]) -> None:
        super().merge_dict(source)
        self._email = source.get("email", self._email)
        self._username = source.get("username", self._username)
        self._password = source.get("password", self._password)
        self._is_admin = source.get("is_admin", self._is_admin)
        self._token = source.get("token", self._token)

    def to_dict(self) -> Dict[str, Any]:
        base_dict = super().to_dict()
        base_dict["email"] = self._email
        base_dict["username"] = self._username
        base_dict["password"] = self._password
        base_dict["is_admin"] = self._is_admin
        base_dict["token"] = self._token
        return base_dict

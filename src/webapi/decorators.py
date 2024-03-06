from functools import wraps

from fastapi import HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from src.webapi.access_security import access_security


def admin_only(func):
    @wraps(func)
    def wrapper(credentials: JwtAuthorizationCredentials = Security(access_security), *args, **kwargs):
        if credentials["role"] != "admin":
            raise HTTPException(status_code=403)
        return func(credentials=credentials, *args, **kwargs)
    return wrapper


def admin_only_async(func):
    @wraps(func)
    async def wrapper(credentials: JwtAuthorizationCredentials = Security(access_security), *args, **kwargs):
        if credentials["role"] != "admin":
            raise HTTPException(status_code=403)
        return await func(credentials=credentials, *args, **kwargs)
    return wrapper


def user_only(func):
    @wraps(func)
    def wrapper(credentials: JwtAuthorizationCredentials = Security(access_security), *args, **kwargs):
        if credentials["role"] != "user":
            raise HTTPException(status_code=403)
        return func(credentials=credentials, *args, **kwargs)
    return wrapper


def user_only_async(func):
    @wraps(func)
    async def wrapper(credentials: JwtAuthorizationCredentials = Security(access_security), *args, **kwargs):
        if credentials["role"] != "user":
            raise HTTPException(status_code=403)
        return await func(credentials=credentials, *args, **kwargs)
    return wrapper

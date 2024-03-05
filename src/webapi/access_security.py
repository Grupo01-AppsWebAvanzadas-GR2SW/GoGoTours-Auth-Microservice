import os
from datetime import timedelta

from dotenv import load_dotenv
from fastapi_jwt import JwtAccessBearer, JwtRefreshBearer
from jose import jwt


load_dotenv("src/.env")
access_security = JwtAccessBearer(
    secret_key=os.getenv("JWT_SECRET_KEY"),
    auto_error=True,
    algorithm=jwt.ALGORITHMS.HS256,
    access_expires_delta=timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))),
    refresh_expires_delta=timedelta(minutes=int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))),
)

refresh_security = JwtRefreshBearer(
    secret_key=os.getenv("REFRESH_SECRET_KEY"),
    auto_error=True,
    algorithm=jwt.ALGORITHMS.HS256,
    refresh_expires_delta=timedelta(minutes=int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES")))
)

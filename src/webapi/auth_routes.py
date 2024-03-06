import os
from datetime import timedelta

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from src.application.auth.dtos.request_reset_password_request_dto import RequestResetPasswordRequestDto
from src.application.auth.dtos.reset_password_request_dto import ResetPasswordRequestDto
from src.application.auth.dtos.user_login_request_dto import UserLoginRequestDto
from src.application.auth.dtos.user_signup_request_dto import UserSignupRequestDto
from src.application.auth.services.login_service_async import LoginServiceAsync
from src.application.auth.services.reset_password_service_async import ResetPasswordServiceAsync
from src.application.auth.services.signup_service_async import SignupServiceAsync
from src.webapi.access_security import access_security, refresh_security
from src.webapi.decorators import admin_only_async, user_only_async

load_dotenv("src/.env")
auth_router = APIRouter()


@auth_router.post('/signup', status_code=201)
async def signup(signup_request: UserSignupRequestDto,
                 signup_service: SignupServiceAsync = Depends(SignupServiceAsync)):
    try:
        await signup_service.signup_user(signup_request)
    except ValueError as e:
        raise HTTPException(status_code=409, detail="User already exists")
    return {'message': 'User created'}


@auth_router.post('/login', status_code=200)
async def login(
        user_login_request: UserLoginRequestDto,
        login_service: LoginServiceAsync = Depends(LoginServiceAsync)
):
    if user := await login_service.login(user_login_request):
        subject = {"user_id": user.id, "username": user.username, "role": "admin" if user.is_admin else "user"}
        return {
            "access_token": access_security.create_access_token(
                subject=subject,
                expires_delta=timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))),
            ),
            "refresh_token": refresh_security.create_refresh_token(
                subject=subject,
                expires_delta=timedelta(minutes=int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))),
            )
        }
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@auth_router.head('/is-logged-in', status_code=200)
async def is_logged_in(
        credentials: JwtAuthorizationCredentials = Security(access_security)
):
    return


@auth_router.post("/refresh")
def refresh(
        credentials: JwtAuthorizationCredentials = Security(refresh_security)
):
    return {
        "access_token": access_security.create_access_token(
            subject=credentials.subject,
            expires_delta=timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))),
        ),
        "refresh_token": refresh_security.create_refresh_token(
            subject=credentials.subject,
            expires_delta=timedelta(minutes=int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))),
        )
    }


@auth_router.head('/is-admin', status_code=200)
@admin_only_async
async def is_admin(
        credentials: JwtAuthorizationCredentials = Security(access_security)
):
    return


@auth_router.head('/is-user', status_code=200)
@user_only_async
async def is_user(
        credentials: JwtAuthorizationCredentials = Security(access_security)
):
    return


@auth_router.post('/request-password-reset', status_code=200)
async def request_password_reset(
        request_reset_password_dto: RequestResetPasswordRequestDto,
        reset_password_service: ResetPasswordServiceAsync = Depends(ResetPasswordServiceAsync)
):
    await reset_password_service.request_reset_password(request_reset_password_dto)
    return {'message': 'Password reset request sent'}


@auth_router.post('/reset-password', status_code=200)
async def reset_password(
        reset_password_dto: ResetPasswordRequestDto,
        reset_password_service: ResetPasswordServiceAsync = Depends(ResetPasswordServiceAsync)
):
    result = await reset_password_service.reset_password(reset_password_dto)
    if not result:
        raise HTTPException(status_code=400, detail="Invalid reset token")
    return {'message': 'Password reset successful'}

from fastapi import APIRouter, Depends, HTTPException

from src.application.auth.dtos.user_login_request_dto import UserLoginRequestDto
from src.application.auth.dtos.user_signup_request_dto import UserSignupRequestDto
from src.application.auth.services.login_service_async import LoginServiceAsync
from src.application.auth.services.signup_service_async import SignupServiceAsync

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
    login_service: LoginServiceAsync = Depends(LoginServiceAsync),
):
    if user := await login_service.login(user_login_request):
        # token = auth.create_access_token(uid=username)
        # return {'access_token': token, 'token_type': 'bearer'}
        return {}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

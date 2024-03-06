from dotenv import load_dotenv
from fastapi import FastAPI

from google.cloud.firestore import AsyncClient

from src.application.auth.repositories.users_repository_async import UsersRepositoryAsync
from src.application.auth.services.login_service_async import LoginServiceAsync
from src.application.auth.services.reset_password_service_async import ResetPasswordServiceAsync
from src.application.auth.services.signup_service_async import SignupServiceAsync
from src.infrastructure.firebase.auth.repositories.firestore_users_repository_async import FirestoreUsersRepositoryAsync
from src.infrastructure.firebase.config.config import initialize_firebase, get_firestore_async
from src.infrastructure.services.auth.default_login_service_async import DefaultLoginServiceAsync
from src.infrastructure.services.auth.default_reset_password_service import DefaultResetPasswordServiceAsync
from src.infrastructure.services.auth.default_signup_service_async import DefaultSignupServiceAsync
from src.webapi.auth_routes import auth_router

initialize_firebase("config/firebase-credentials.json")
load_dotenv("src/.env")
app = FastAPI()
app.dependency_overrides = {
    AsyncClient: get_firestore_async,
    UsersRepositoryAsync: FirestoreUsersRepositoryAsync,
    LoginServiceAsync: DefaultLoginServiceAsync,
    SignupServiceAsync: DefaultSignupServiceAsync,
    ResetPasswordServiceAsync: DefaultResetPasswordServiceAsync
}
app.include_router(auth_router)

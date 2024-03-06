from dotenv import load_dotenv
from fastapi import FastAPI

from google.cloud.firestore import AsyncClient

from application.auth.repositories.users_repository_async import UsersRepositoryAsync
from application.auth.services.login_service_async import LoginServiceAsync
from application.auth.services.reset_password_service_async import ResetPasswordServiceAsync
from application.auth.services.signup_service_async import SignupServiceAsync
from infrastructure.firebase.auth.repositories.firestore_users_repository_async import FirestoreUsersRepositoryAsync
from infrastructure.firebase.config.config import initialize_firebase, get_firestore_async
from infrastructure.services.auth.default_login_service_async import DefaultLoginServiceAsync
from infrastructure.services.auth.default_reset_password_service import DefaultResetPasswordServiceAsync
from infrastructure.services.auth.default_signup_service_async import DefaultSignupServiceAsync
from webapi.auth_routes import auth_router

initialize_firebase("/etc/secrets/firebase-credentials.json")
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

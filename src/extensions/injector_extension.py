from flask_injector import FlaskInjector
from injector import singleton, Binder
from google.cloud.firestore import AsyncClient

from src.application.auth.repositories.users_repository_async import UsersRepositoryAsync
from src.application.auth.services.login_service_async import LoginServiceAsync
from src.application.auth.services.signup_service_async import SignupServiceAsync
from src.application.auth.services.reset_password_service_async import ResetPasswordServiceAsync
from src.application.chat.repositories.conversations_repository_async import ConversationsRepositoryAsync
from src.application.tourist_packages.repositories.tourist_packages_repository_async import \
    TouristPackagesRepositoryAsync
from src.application.reserves.repositories.reserve_repository_async import ReservesRepositoryAsync
from src.application.chat.services.chat_service_async import ChatServiceAsync
from src.application.tourist_packages.services.tourist_packages_service_async import TouristPackagesServiceAsync
from src.application.reserves.services.reserve_service_async import ReservesServiceAsync
from src.infrastructure.firebase.config.config import get_firestore_async
from src.infrastructure.firebase.auth.repositories.firestore_users_repository_async import FirestoreUsersRepositoryAsync
from src.infrastructure.services.auth.default_login_service_async import DefaultLoginServiceAsync
from src.infrastructure.services.auth.default_signup_service_async import DefaultSignupServiceAsync
from src.infrastructure.services.auth.default_reset_password_service import DefaultResetPasswordServiceAsync
from src.infrastructure.firebase.chat.repositories.firestore_conversations_repository_async import FirestoreConversationsRepositoryAsync
from src.infrastructure.firebase.tourist_packages.repositories.firestore_tourist_packages_repository_async import \
    FirestoreTouristPackagesRepositoryAsync
from src.infrastructure.firebase.reserves.repositories.firestore_reserves_repository_async import \
    FirestoreReservesRepositoryAsync
from src.infrastructure.services.chat.default_chat_service_async import DefaultChatServiceAsync
from src.infrastructure.services.tourist_packages.default_tourist_packages_service_async import \
    DefaultTouristPackagesServiceAsync
from src.infrastructure.services.reserves.default_reserves_service_async import DefaultReservesSeviceAsync


def configure_binding(binder: Binder) -> Binder:
    binder.bind(AsyncClient, to=get_firestore_async, scope=singleton)
    binder.bind(ConversationsRepositoryAsync, to=FirestoreConversationsRepositoryAsync, scope=singleton)
    binder.bind(ChatServiceAsync, to=DefaultChatServiceAsync, scope=singleton)
    binder.bind(TouristPackagesRepositoryAsync, to=FirestoreTouristPackagesRepositoryAsync, scope=singleton)
    binder.bind(TouristPackagesServiceAsync, to=DefaultTouristPackagesServiceAsync, scope=singleton)
    binder.bind(ReservesRepositoryAsync, to=FirestoreReservesRepositoryAsync, scope=singleton)
    binder.bind(ReservesServiceAsync, to=DefaultReservesSeviceAsync, scope=singleton)
    binder.bind(UsersRepositoryAsync, to=FirestoreUsersRepositoryAsync, scope=singleton)
    binder.bind(LoginServiceAsync, to=DefaultLoginServiceAsync, scope=singleton)
    binder.bind(SignupServiceAsync, to=DefaultSignupServiceAsync, scope=singleton)
    binder.bind(ResetPasswordServiceAsync, to=DefaultResetPasswordServiceAsync, scope=singleton)
    return binder


def register_dependency_injection(app) -> None:
    FlaskInjector(app=app, modules=[configure_binding])

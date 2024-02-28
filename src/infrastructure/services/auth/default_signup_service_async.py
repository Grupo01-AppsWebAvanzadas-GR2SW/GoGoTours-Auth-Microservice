from src.domain.auth.entities.user import User
from src.application.auth.services.signup_service_async import SignupServiceAsync
from src.application.auth.dtos.user_signup_request_dto import UserSignupRequestDto
from src.application.auth.dtos.user_response_dto import UserResponseDto
from src.application.auth.repositories.users_repository_async import UsersRepositoryAsync
from injector import inject
import bcrypt


class DefaultSignupServiceAsync(SignupServiceAsync):
    @inject
    def __init__(self, users_repository_async: UsersRepositoryAsync):
        self._users_repository_async = users_repository_async

    async def signup_user(self, signup_request: UserSignupRequestDto):
        # Verificar si el usuario ya existe en el repositorio (usando su email u otro identificador único)
        existing_user = await self._users_repository_async.get_user_by_email(signup_request.email)
        if existing_user:
            raise ValueError('El usuario ya está registrado')

        # Hashear la contraseña antes de almacenarla en la base de datos
        hashed_password = bcrypt.hashpw(signup_request.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Crear una instancia de la entidad User
        new_user = User(email=signup_request.email, password=hashed_password, username=signup_request.username)

        # Guardar el nuevo usuario en el repositorio
        await self._users_repository_async.create_user(new_user)

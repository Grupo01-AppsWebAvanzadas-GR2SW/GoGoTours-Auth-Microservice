import os
import urllib.parse

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import bcrypt
from fastapi import Depends
from itsdangerous import URLSafeTimedSerializer

from src.application.auth.dtos.request_reset_password_request_dto import RequestResetPasswordRequestDto
from src.application.auth.dtos.reset_password_request_dto import ResetPasswordRequestDto
from src.application.auth.repositories.users_repository_async import UsersRepositoryAsync
from src.application.auth.services.reset_password_service_async import ResetPasswordServiceAsync
from src.infrastructure.smtp.config.config import connect_smtp_server


class DefaultResetPasswordServiceAsync(ResetPasswordServiceAsync):
    def __init__(
            self,
            users_repository_async: UsersRepositoryAsync = Depends(UsersRepositoryAsync)
    ):
        self._users_repository_async = users_repository_async

    async def request_reset_password(self, reset_request: RequestResetPasswordRequestDto) -> None:
        user = await self._users_repository_async.get_user_by_email(reset_request.email)
        if user is not None:
            reset_token = await self.generate_reset_token(reset_request.email)
            user.token = reset_token
            user.set_updated_at_now()
            print(user.id)
            await self._users_repository_async.update_async(user)

            # Enviar el correo electrónico con el token de restablecimiento
            await self.send_reset_email(reset_request.email, reset_token)

    async def reset_password(self, reset_request: ResetPasswordRequestDto) -> bool:
        user = await self._users_repository_async.get_user_by_reset_token(reset_request.reset_token)
        if user:
            hashed_password = bcrypt.hashpw(reset_request.new_password.encode('utf-8'), bcrypt.gensalt()).decode(
                'utf-8')
            user.password = hashed_password
            user.token = None
            user.set_updated_at_now()
            await self._users_repository_async.update_async(user)
            return True
        return False

    async def check_user_exists(self, email):
        existing_user = await self._users_repository_async.get_user_by_email(email)
        return existing_user is not None

    async def generate_reset_token(self, email):
        secret_key = os.getenv("PASSWORD_RESET_KEY")

        # Crea un serializador con una clave secreta y un salt único
        serializer = URLSafeTimedSerializer(secret_key, salt=f"reset-salt-{os.getenv("PASSWORD_RESET_SALT")}]")

        # Genera el token utilizando el correo electrónico del usuario
        token = serializer.dumps(email, salt=f"reset-salt-{os.getenv("PASSWORD_RESET_SALT")}]")

        return token

    async def send_reset_email(self, email, reset_token):
        try:
            subject = "Restablecimiento de contraseña"
            body = f"Se ha solicitado restablecer la contraseña de su cuenta. \
                        \nPor favor, haga clic en el siguiente enlace para restablecer su cuenta:\
                        \n{os.getenv("FRONTEND_URL")}/reset-password?token={urllib.parse.quote(reset_token, safe='')}]\
                        \
                        \n\nSi no solicito restablecer su contraseña, ignore este correo electrónico.\
                        "

            message = MIMEMultipart()
            message.attach(MIMEText(body, 'plain'))
            message['Subject'] = subject
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                connect_smtp_server(server)
                server.sendmail(os.getenv("SMTP_USERNAME"), [email], message.as_string())

        except Exception as e:
            print(e)
            return

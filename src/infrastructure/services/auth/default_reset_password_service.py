from flask import url_for
from application.auth.dtos.reset_password_request_dto import ResetPasswordRequestDto
from application.auth.services.reset_password_service_async import ResetPasswordServiceAsync
from src.application.auth.repositories.users_repository_async import UsersRepositoryAsync
from injector import inject
import bcrypt
import string
import secrets
from itsdangerous import URLSafeTimedSerializer
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class DefaultResetPasswordServiceAsync(ResetPasswordServiceAsync):
    @inject
    def __init__(self, users_repository_async: UsersRepositoryAsync):
        self._users_repository_async = users_repository_async

    async def request_reset_password(self, reset_request: ResetPasswordRequestDto) -> None:
        user = await self._users_repository_async.get_user_by_email(reset_request.email)
        if user:
            reset_token = await self.generate_reset_token(reset_request.email)

            user.reset_token = reset_token
            await self._users_repository_async.update_user(user)

            # Enviar el correo electrónico con el token de restablecimiento
            await self.send_reset_email(reset_request.email, reset_token)

    async def reset_password(self, reset_token: str, new_password: str) -> bool:
        user = await self._users_repository_async.get_user_by_reset_token(reset_token)
        if user:
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user.password = hashed_password
            user.reset_token = None
            await self._users_repository_async.update_user(user)
            return True
        return False

    async def check_user_exists(self, email):
        existing_user = await self._users_repository_async.get_user_by_email(email)
        return existing_user is not None

    async def generate_reset_token(self, email):
        secret_key = "secret_key"

        # Crea un serializador con una clave secreta y un salt único
        serializer = URLSafeTimedSerializer(secret_key, salt="reset-salt")

        # Genera el token utilizando el correo electrónico del usuario
        token = serializer.dumps(email, salt="reset-salt")
        print("token: "+token)

        user = await self._users_repository_async.get_user_by_email(email)
        if user:
            user.token = token
            user.set_updated_at_now()
            await self._users_repository_async.update_user(user)

        return token

    async def send_reset_email(self, email, reset_token):
        try:
            # Configuración del servidor SMTP (ajusta los valores según tu proveedor de correo electrónico)
            smtp_server = "smtp.example.com"
            smtp_port = 587
            smtp_username = "your_username"
            smtp_password = "your_password"

            # Crea el mensaje de correo electrónico
            subject = "Restablecimiento de contraseña"
            reset_url = url_for('reset_password_succesful', token=reset_token, _external=True)
            body = f"Haz clic en el siguiente enlace para restablecer tu contraseña: {reset_url}"

            message = MIMEMultipart()
            message.attach(MIMEText(body, 'plain'))
            message['Subject'] = subject

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, [email], message.as_string())

        except Exception as e:
            print(f"Error al enviar el correo electrónico: {str(e)}")

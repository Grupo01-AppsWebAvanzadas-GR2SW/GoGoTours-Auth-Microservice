from flask import render_template, request, redirect, url_for, session
from flask.views import MethodView
from injector import inject
from src.application.auth.services.reset_password_service_async import ResetPasswordServiceAsync
from src.application.auth.dtos.reset_password_request_dto import ResetPasswordRequestDto


class ResetPasswordView(MethodView):
    @inject
    def __init__(self, reset_password_service: ResetPasswordServiceAsync):
        self._reset_password_service = reset_password_service

    def get(self):
        if session.get("id") is not None:
            return redirect(url_for("home"))
        return render_template("auth/reset_password.html")

    async def post(self):
        email = request.form.get("email")

        user_exists = await self._reset_password_service.check_user_exists(email)
        if not user_exists:
            return render_template("auth/reset_password.html",
                                   error="El correo electrónico proporcionado no está registrado.")

        # Generar un token de reseteo de contraseña (puedes usar Firebase Authentication para esto)
        reset_token = await self._reset_password_service.generate_reset_token(email)

        # Enviar el token al correo del usuario (Firebase Authentication o servicios de email)
        await self._reset_password_service.send_reset_email(email, reset_token)

        return redirect(url_for('reset_password_successful'))

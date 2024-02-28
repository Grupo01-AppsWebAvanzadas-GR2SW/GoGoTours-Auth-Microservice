from flask import render_template, request, flash, url_for, redirect
from flask.views import MethodView
from injector import inject
from src.application.auth.services.reset_password_service_async import ResetPasswordServiceAsync


class ResetPasswordSuccessfulView(MethodView):
    @inject
    def __init__(self, reset_password_service: ResetPasswordServiceAsync):
        self._reset_password_service = reset_password_service

    def get(self):
        return render_template("auth/reset_password_successful.html")

    async def post(self):
        try:
            reset_token = request.form.get("reset_token")
            new_password = request.form.get("new_password")

            await self._reset_password_service.reset_password(reset_token, new_password)

            return redirect(url_for("login"))

        except Exception as e:
            # Manejar errores y mostrar un mensaje de error si es necesario

            return redirect(url_for("login"))

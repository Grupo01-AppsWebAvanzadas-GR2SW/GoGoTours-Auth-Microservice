from flask import render_template, request, redirect, url_for, session
from flask.views import MethodView
from injector import inject
from src.application.auth.services.signup_service_async import SignupServiceAsync
from src.application.auth.dtos.user_signup_request_dto import UserSignupRequestDto


class SignupView(MethodView):
    @inject
    def __init__(self, signup_service: SignupServiceAsync):
        self._signup_service = signup_service

    def get(self):
        if session.get("id") is not None:
            return redirect(url_for("home"))
        return render_template("auth/signup.html")

    async def post(self):
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        try:
            if password != confirm_password:
                raise ValueError("Las contraseñas no coinciden")

            user_dto = UserSignupRequestDto(username=username, email=email, password=password)
            await self._signup_service.signup_user(user_dto)

            return redirect(url_for("login"))

        except ValueError as e:
            error_msg = str(e)
            return render_template("auth/signup.html", error=error_msg,
                                   username=username, email=email)

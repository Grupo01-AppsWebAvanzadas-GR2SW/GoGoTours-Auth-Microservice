from flask.views import MethodView
from extensions.decorations_extension import login_required
from flask import session, redirect, url_for


class LogoutView(MethodView):

    @login_required
    def get(self):
        session.clear()
        return redirect(url_for("login"))

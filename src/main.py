import uvicorn
from asgiref.wsgi import WsgiToAsgi
from flask import Flask
from src.infrastructure.firebase.config.config import initialize_firebase
from src.extensions.injector_extension import register_dependency_injection
from src.extensions.views_extension import register_views


Flask.url_for.__annotations__ = {}
app = Flask(__name__, template_folder="web/templates", static_folder="web/static")
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "secret_key"
initialize_firebase("../config/firebase-credentials.json")
register_views(app)
register_dependency_injection(app)
asgi_app = WsgiToAsgi(app)


if __name__ == "__main__":
    uvicorn.run("main:asgi_app", host="127.0.0.1", port=5000, reload=True)

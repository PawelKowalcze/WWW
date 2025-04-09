from flask import Flask
from .main.routes import main
from .auth.routes import auth
from .dashboard.routes import dashboard


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'

    # Rejestracja blueprintów
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(dashboard, url_prefix='/dashboard')

    return app
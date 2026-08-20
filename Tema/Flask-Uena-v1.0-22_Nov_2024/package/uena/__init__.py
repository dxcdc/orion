from flask import Flask
from .routes import main as main_blueprint


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'oJew_hVN9dv46ZkLReHCVw'
    app.secret_key = 'oJew_hVN9dv46ZkLReHCVw'

    app.register_blueprint(main_blueprint)

    return app  
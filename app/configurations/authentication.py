from flask import Flask
from flask_login import LoginManager
from app.models.usuarios_model import UsuariosModel

def init_app(app: Flask):
    login_manager = LoginManager(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def user_loader(user_id):
        return UsuariosModel.query.get(user_id)
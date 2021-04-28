from flask import Flask 
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.usuarios_model import UsuariosModel
    from app.models.projetos_model import ProjetosModel
    from app.models.integrantes_model import IntegrantesModel
    from app.models.security_model import TokenModel
    from app.models.solicitacoes_model import SolicitacoesModel

    
    
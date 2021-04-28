from . import db
from flask_login import UserMixin

class UsuariosModel(db.Model, UserMixin): 
    __tablename__ = "usuarios"
    
    id = db.Column(db.Integer, primary_key=True)
    
    nome = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False, unique=False)
    tecnologias = db.Column(db.String(100), nullable=True, unique=False)
    idiomas = db.Column(db.String(100), nullable=True, unique=False)
    bio = db.Column(db.String(1000), nullable=True, unique=False)

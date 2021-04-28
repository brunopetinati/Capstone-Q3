from flask import Blueprint, request, current_app
from app.models.usuarios_model import UsuariosModel
from http import HTTPStatus

import bcrypt

bp_register = Blueprint("bp_register", __name__, url_prefix="/api")



@bp_register.route('/register', methods=['POST'])
def usuarios():
    
    session = current_app.db.session 

    data = request.get_json()

    hashed = bcrypt.hashpw(data["senha"].encode("utf-8"), bcrypt.gensalt())
    hashed = hashed.decode("utf-8", "ignore")

    usuario = UsuariosModel(
        nome=data["nome"],
        senha=hashed,
        email=data["email"],
        tecnologias=data["tecnologias"],
        idiomas=data["idiomas"],
        bio=data["bio"]
    )

    session.add(usuario) 
    session.commit() 

    return {"id": usuario.id, "nome": usuario.nome, "email": usuario.email, 
    "tecnologias": usuario.tecnologias, "idiomas": usuario.idiomas, "bio": usuario.bio}, HTTPStatus.CREATED


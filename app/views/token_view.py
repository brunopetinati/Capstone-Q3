from flask import Blueprint, request, current_app
from http import HTTPStatus
from random import randint
from app.models.security_model import TokenModel
from app.models.usuarios_model import UsuariosModel


bp_token = Blueprint("bp_token", __name__, url_prefix="/api")

@bp_token.route('/obtain_token', methods=['POST'])
def obtain_token():

    data = request.get_json()

    email_r =  data['email']
    senha_r = data['senha']

    found_email_by_r = UsuariosModel.query.filter_by(email=email_r).first()
    found_password_by_r = UsuariosModel.query.filter_by(senha=senha_r).first()

    token = randint(0,1000000000)

    token_model = TokenModel(user=data['email'], token=token)

    session = current_app.db.session
    session.add(token_model)
    session.commit()


    if found_email_by_r and found_password_by_r:
            if email_r == found_email_by_r.email and senha_r == found_password_by_r.senha:   
                return {"message":"Congrats! You have logged in! Welcome into our platform",
                "token": token}
    
    else: 
        return {"Mensagem":"Algo deu errado! =O"}, 422
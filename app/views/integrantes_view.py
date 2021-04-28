from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.integrantes_model import IntegrantesModel
from app.models.projetos_model import ProjetosModel
from app.models.usuarios_model import UsuariosModel
from app.models.security_model import TokenModel


bp_integrantes = Blueprint("bp_integrantes", __name__, url_prefix="/api")

@bp_integrantes.route('/integrantes', methods=["POST"])
def integrantes():
    

    session = current_app.db.session

    data = request.get_json()

    try:
        token = request.headers['auth-token']
        extant_token = TokenModel.query.filter_by(token=token).first()
    except:
        return {"Mensagem":"Um token é necessário! Tente logar :)"}, 401

    # quem ta logado é o dono da tabela. então o token corresponde ao seu e-mail. é necessario que o projeto
    # contenha algo correspondete com o seu email

    
    try:
        projeto = ProjetosModel.query.filter_by(id=data['projeto_id']).first()
        usuario = UsuariosModel.query.filter_by(id=data['usuario_id']).first()

        if extant_token.user == projeto.owner_id:
            
            try:
                integrantes = IntegrantesModel(projeto_id=data['projeto_id'], usuario_id=data['usuario_id'], projeto=projeto.nome, usuario=usuario.email,)

                session.add(integrantes)
                session.commit()
            except:
                return {"Mensagem":"Usuário ou Projeto não encontrado"}, 422

            
            
            return {
                "id": integrantes.id,
                "projeto": projeto.nome,
                "usuario": usuario.nome
            }, HTTPStatus.CREATED

        else:
            return {"Mensagem":"Talvez você tenha tentado registrar um usuário em um projeto que não é seu :)"}, 401

    except:
        return {"Mensagem":"Usuário ou Projeto não encontrado"}, 401




    
    
    


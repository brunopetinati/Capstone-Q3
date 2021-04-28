from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.projetos_model import ProjetosModel
from app.models.security_model import TokenModel

bp_projetos = Blueprint("bp_projetos", __name__, url_prefix="/api")

@bp_projetos.route('/projetos', methods=["POST"])
def projetos():

    

    data = request.get_json()
    
    #se o email do usuario na ProjetosModel = token de usuario por busca email na tabela TokenModel


    try:
        token = request.headers['auth-token']
        session = current_app.db.session
        extant_token = TokenModel.query.filter_by(token=token).first()


        projeto = ProjetosModel(
        nome = data["nome"],
        categoria = data["categoria"],
        objetivo = data["objetivo"],
        descricao = data["descricao"],
        owner_id = extant_token.user
        )


        if extant_token:
            session.add(projeto)
            session.commit()

        else:
            return {'Mensagem':'Um token é necessário. Tente logar primeiro.'}, 401
    except:
        return {'Mensagem':'Um token é necessário. Tente logar primeiro.'}, 401

    data['id'] = projeto.id

    return data, HTTPStatus.CREATED

@bp_projetos.route('/projetos', methods=["GET"])
def lista_projetos():
    session = current_app.db.session

    lista_de_projetos = ProjetosModel.query.all()

    return { "data": [{"id": p.id, 
    "nome": p.nome,
    "categoria": p.categoria,
    "objetivo": p.objetivo,
    "descricao": p.descricao} for p in lista_de_projetos]}, HTTPStatus.OK

from flask import Blueprint, request, current_app
from http import HTTPStatus
from app.models.solicitacoes_model import SolicitacoesModel
from app.models.security_model import TokenModel

bp_solicitacoes = Blueprint("bp_solicitacoes", __name__, url_prefix="/api")

@bp_solicitacoes.route('/solicitacoes', methods=["POST"])
def solicitacoes():

    data = request.get_json()
    
    #se o email do usuario na ProjetosModel = token de usuario por busca email na tabela TokenModel


    try:
        token = request.headers['auth-token']
        session = current_app.db.session
        extant_token = TokenModel.query.filter_by(token=token).first()
        print(extant_token.__dict__)

        solicitacao = SolicitacoesModel(
        projeto_id = data['projeto_id'],
        solicitante = extant_token.id,
        user_email = extant_token.user
        )


        if extant_token:
            session.add(solicitacao)
            session.commit()
        else:
            return {'Mensagem':'Um token é necessário. Tente logar primeiro.'}, 401
    except:
        return {'Mensagem':'Algo deu errado. Verifique as informações'}, 422

    

    return {"Mensagem":"Solicitação registrada com sucesso!"}, HTTPStatus.CREATED
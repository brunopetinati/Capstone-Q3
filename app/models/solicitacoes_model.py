# através do meu token, pegará meu nome de usuário para solicitação
# nome do projeto será chave estrangeira

from . import db



class SolicitacoesModel(db.Model):
    __tablename__ = 'solicitacoes'

    id = db.Column(db.Integer, primary_key=True) 
    projeto_id = db.Column(db.Integer, db.ForeignKey('projetos.id', onupdate='CASCADE', ondelete='CASCADE')) 
    solicitante = db.Column(db.Integer, db.ForeignKey('token.id', onupdate='CASCADE', ondelete='CASCADE'))
    user_email = db.Column(db.String, db.ForeignKey('usuarios.email', onupdate='CASCADE', ondelete='CASCADE'))
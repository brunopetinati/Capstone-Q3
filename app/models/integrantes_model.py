from . import db



class IntegrantesModel(db.Model):
    __tablename__ = 'integrantes'


    id = db.Column(db.Integer, primary_key=True) 

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', onupdate='CASCADE', ondelete='CASCADE'))

    projeto_id = db.Column(db.Integer, db.ForeignKey('projetos.id', onupdate='CASCADE', ondelete='CASCADE')) 

    projeto = db.Column(db.String, nullable=False)

    usuario = db.Column(db.String, db.ForeignKey('usuarios.email', onupdate='CASCADE', ondelete='CASCADE'))

    


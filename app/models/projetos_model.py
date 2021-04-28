from . import db

class ProjetosModel(db.Model):
    __tablename__ = "projetos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    categoria = db.Column(db.String, nullable=False)
    objetivo = db.Column(db.Text, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.String, db.ForeignKey('usuarios.email', onupdate='CASCADE', ondelete='CASCADE'))

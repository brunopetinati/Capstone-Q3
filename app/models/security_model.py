from . import db


class TokenModel(db.Model): 
    __tablename__ = "token"
    
    id = db.Column(db.Integer, primary_key=True)    
    user = db.Column(db.String(100), nullable=False, unique=False)
    token = db.Column(db.Integer, nullable=False, unique=True)
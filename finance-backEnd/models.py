from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__="usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    is_admin=db.Column(db.Boolean, default=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)


class Gasto(db.Model):
    __Gastos__="Gastos"
    
    id = db.Column(db.Integer, primary_key = True)
    descricao = db.Column(db.String(120), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.String(10), nullable=False)
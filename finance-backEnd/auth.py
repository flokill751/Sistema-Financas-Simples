from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_bcrypt import create_access_token
from models import db,Usuario

auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth.route('/register', methods=['POST'])

def register():
    data = request.get()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')

    if Usuario.query.filter_by(email=email).first():
        return jsonify({"error": "Email já cadastrado"}), 409
    
@auth.route('/logon', methods=['POST'])

def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    Usuario = Usuario.query.filter_by(email=email).first()
    if not Usuario or not bcrypt.check_password_hash(Usuario.senha_hash, senha):
        return jsonify({"error":"Credenciais inválidas"}), 401
    access_tocken = create_access_token(identity=Usuario.id)
    return  jsonify({"access_token": access_token}), 200
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import Usuario, db
from extensions import bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')

    if Usuario.query.filter_by(email=email).first():
        return jsonify({"error": "Email já cadastrado"}), 409

    senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

    novo_usuario = Usuario(nome=nome, email=email, senha_hash=senha_hash)
    db.session.add(novo_usuario)
    db.session.commit()

    return jsonify({"message": "Usuário registrado com sucesso"}), 201

@auth.route('/logon', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    usuario = Usuario.query.filter_by(email=email).first()
    if not usuario or not bcrypt.check_password_hash(usuario.senha_hash, senha):
        return jsonify({"error": "Credenciais inválidas"}), 401

    access_token = create_access_token(identity=usuario.id)
    return jsonify({"access_token": access_token}), 200

@auth.route("/perfil", methods=["GET"])
@jwt_required()
def perfil():
    user_id = get_jwt_identity()
    usuario = Usuario.query.get(user_id)

    if not usuario:
        return jsonify({"error": "Usuário não encontrado"}), 404

    return jsonify({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email
    }), 200

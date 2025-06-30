from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from extensions import bcrypt, db, jwt
from auth import auth

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:senha123@localhost/financa_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "sua_chave_secreta"

bcrypt.init_app(app)
db.init_app(app)
jwt.init_app(app)

app.register_blueprint(auth, url_prefix='/auth')

with app.app_context():
    db.create_all()

UPLOAD_FOLDER = "arquivoSave"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")  
def home():
    return "Conexão com banco SQL funcionando!)"

@app.route("/arquivoSave", methods=["POST"])
def arquivo_file():
    if "file" not in request.files:
        return {"error": "Nenhum arquivo enviado"}, 400

    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return {"message": f"Arquivo {file.filename} salvo com sucesso !"}

if __name__ == "__main__":
    app.run(debug=True)

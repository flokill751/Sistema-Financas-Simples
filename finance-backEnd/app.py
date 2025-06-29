from flask import Flask, request, jsonify 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db
import os 

app = Flask(__name__)
CORS(app)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:senha123@localhost/financa_db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")  
def home():
    return "Conexão com banco SQL funcionando!)"

UPLOAD_FOLDER = "arquivoSave"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route ("/arquivoSave", methods=["POST"])
def arquivo_file():
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400


    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify ({"message": f"Arquivo {file.filename} salvo com sucesso !"})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask_cors import CORS
from flask import render_template, jsonify, request, send_file
from pdf_generator import gerar_pdf
from modelo_flask_db import Tarefas
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
# ---- Informações do banco do Pablo aqui!
DB_USER = 'seu_usuario_aqui'
DB_PASSWORD = 'sua_senha_aqui'
DB_HOST = 'localhost' # ou o host onde seu DB está
DB_PORT = '5432'      # porta padrão do Postgres
DB_NAME = 'tarefas_db' # o banco que você criou
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Rotas ----------------------------
@app.route("/")
def homepage():
    return render_template("Arquivo")


@app.route("/tarefas", methods=["GET"])
def pegar_tarefa():
    tarefas = Tarefas.query.all() #Pesquisa no banco de dados
    tarefas_json = list(map(lambda x: x.to_json() , tarefas)) #list comprehension
   
    return jsonify({"tarefas": tarefas_json}) #Retornar jsonify com resposta do banco de dados


@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    tarefa = request.get_json()

    if not tarefa or not "titulo" in tarefa:
        return jsonify({"erro": "O titulo da tarefa é obrigatório"}), 400 # 400 = Bad Request
    
    #Criar tarefa e registrar no banco

    return jsonify("Tarefa aqui"), 201 


@app.route("/tarefa/PDF", methods=["GET"])
def pegar_tarefa_pdf():
    tarefas = "Pegar todas as tarefas do banco de dados"

    pdf_buffer = gerar_pdf(tarefas) # Essa função vem do arquivo pdf_generator

    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name='relatorio_tarefas.pdf',
        mimetype='application/pdf'
    )


#Executar API ----------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug = True) # <---Debug ativado!

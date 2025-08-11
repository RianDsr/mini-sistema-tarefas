from flask import render_template, jsonify, request, send_file
from config import db, app
from modelo_flask_db import Tarefas
from pdf_generator import gerar_pdf



# Rotas ----------------------------
@app.route("/")
def homepage():
    return "Aqui é a homepage"


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

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug = True) # <---Debug ativado!
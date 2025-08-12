from flask import render_template, jsonify, request, send_file
from config import db, app
from modelo_flask_db import Tarefas
from pdf_generator import gerar_pdf



# Rotas ----------------------------
@app.route("/")
def homepage():
    return "Aqui é a homepage"

#----   OBS: Ver se o rian vai querer uma tarefa especifica ou todas as tarefas. Se quiser os dois fazer mais uma rota GET para a busca de uma tarefa individual pelo ID
@app.route("/tarefas", methods=["GET"])
def pegar_tarefa():
    tarefas = Tarefas.query.all() #Pesquisa no banco de dados
    tarefas_json = list(map(lambda x: x.to_json() , tarefas)) #list comprehension
   
    return jsonify({"tarefas": tarefas_json}) #Retornar jsonify com resposta do banco de dados


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    titulo = request.json.get("titulo")

    if not titulo:
        return jsonify({"erro": "O titulo da tarefa é obrigatório"}), 400 # 400 = Bad Request
    
    descricao = request.json.get("descricao")
    nova_tarefa = Tarefas(titulo=titulo,descricao=descricao)
    try:
        db.session.add(nova_tarefa)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}) , 400
    
    return jsonify({"mensagem":"tarefa criada"}), 201 #Perguntar pro rian se ele vai querer o que foi criado e alterar caso necessário


@app.route("/tarefa/PDF", methods=["GET"])
def pegar_tarefa_pdf():
    tarefas = Tarefas.query.all()
    tarefas_json = list(map(lambda x: x.to_json() , tarefas))
    pdf_buffer = gerar_pdf(tarefas_json) # Essa função vem do arquivo pdf_generator


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
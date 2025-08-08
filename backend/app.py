from flask import Flask
from flask_cors import CORS

#Bibliotecas das rotas ----------

from flask import render_template, jsonify, request, send_file
from fpdf import FPDF
import io

app = Flask(__name__)
CORS(app)

#Rotas ----------------------------
@app.route("/")
def homepage():
    return "Página aqui"

@app.route("/tarefa", methods=["GET"])
def pegar_tarefa():
    #Pesquisar no banco de dados
    tarefas = "PESQUISA BANCO DE DADOS"
    for tarefa in tarefas:
        None
    return(jsonify()) #Retornar jsonify com resposta do banco de dados

@app.route("/tarefa", methods=["POST"])
def adicionar_tarefa():
    tarefa = request.get_json()

    if not tarefa or not "titulo" in tarefa:
        return jsonify({"erro": "O titulo da tarefa é obrigatório"}), 400 # 400 = Bad Request
    
    #Criar tarefa e registrar no banco

    return jsonify("Tarefa aqui"), 201 


@app.route("/tarefa/PDF", methods=["GET"])
def pegar_tarefa_pdf():
    tarefas = "PEQUISA NO BANCO DE DADOS AQUI"

    pdf = FPDF()
    pdf.add_page()
    
    # Título do PDF
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Relatório de Tarefas', ln=True, align='C')
    pdf.ln(10) # Pula uma linha
    
    # Cabeçalhos da tabela
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(60, 10, 'Título', 1)
    pdf.cell(130, 10, 'Descrição', 1, ln=True)

        # Dados das tarefas
    pdf.set_font('Arial', '', 12)
    for tarefa in tarefas:
        # Usar multi_cell para quebrar a linha automaticamente se o texto for grande
        pdf.multi_cell(60, 10, tarefa.title.encode('latin-1', 'replace').decode('latin-1'), border=1)
        # Manter a posição Y para a próxima célula na mesma linha
        y_pos = pdf.get_y()
        pdf.set_xy(70, y_pos - 10) # 10 (margem) + 60 (largura da celula anterior)
        pdf.multi_cell(130, 10, tarefa.description.encode('latin-1', 'replace').decode('latin-1'), border=1)

    # Salva o PDF em um buffer de memória em vez de um arquivo físico
    pdf_buffer = io.BytesIO(pdf.output(dest='S').encode('latin-1'))
    
    return send_file(
        pdf_buffer,
        as_attachment=True,
        download_name='relatorio_tarefas.pdf',
        mimetype='application/pdf'
    )


#Executar API ----------------------
if __name__ == "__main__":
    app.run(debug = True) # <---Debug ativado!

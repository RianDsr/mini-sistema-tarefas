from flask import Flask
from flask_cors import CORS

#Bibliotecas das rotas ----------

from flask import render_template, jsonify, request, send_file
from fpdf import FPDF
import io

#Biblioteca do banco ----------
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)

# --- ALTERAÇÃO PRINCIPAL: Configuração do Banco de Dados PostgreSQL ---
# O formato é: "postgresql://usuario:senha@host:porta/nome_do_banco"
# Substitua com suas credenciais reais do PostgreSQL.
DB_USER = 'seu_usuario_aqui'
DB_PASSWORD = 'sua_senha_aqui'
DB_HOST = 'localhost' # ou o host onde seu DB está
DB_PORT = '5432'      # porta padrão do Postgres
DB_NAME = 'tarefas_db' # o banco que você criou

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }

# --- Bloco para criar a tabela (se não existir) ---
with app.app_context():
    db.create_all()

# --- Rotas da API (NÃO MUDAM NADA AQUI!) ---
# Todo o código das rotas que você já viu continua exatamente o mesmo,
# pois ele interage com o `db`, e o SQLAlchemy se encarrega de "traduzir"
# os comandos para o dialeto do PostgreSQL.


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

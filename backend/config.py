from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

"""
# ---- Informações do banco do Pablo aqui!
DB_USER = 'seu_usuario_aqui'
DB_PASSWORD = 'sua_senha_aqui'
DB_HOST = 'localhost' # ou o host onde seu DB está
DB_PORT = '5432'      # porta padrão do Postgres
DB_NAME = 'tarefas_db' # o banco que você criou
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
"""
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mydatabase.db" #Apenas para teste
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Apenas para teste

db = SQLAlchemy(app)
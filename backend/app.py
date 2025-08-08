from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import sqlite3
from pdf_generator import generate_tasks_pdf

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (title, description) VALUES (?, ?)',
                 (data['title'], data['description']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Tarefa adicionada com sucesso!'})

@app.route('/tasks/pdf', methods=['GET'])
def generate_pdf():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    filename = generate_tasks_pdf([dict(t) for t in tasks])
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
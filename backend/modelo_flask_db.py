from config import db

class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.String(350), nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
        }

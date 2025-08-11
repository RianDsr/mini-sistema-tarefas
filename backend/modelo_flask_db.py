from config import db

class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descrição = db.Column(db.String(350), nullable=True)

    def to_json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descrição": self.descrição,
        }

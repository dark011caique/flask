from jogoteca import db

class Jogos(db.Model):
    __tablename__ = 'jogos'  # força nome da tabela

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Jogo {self.nome}>'

class Usuario(db.Model):
    __tablename__ = 'usuarios'  # força nome da tabela

    nickname = db.Column(db.String(8), primary_key=True, nullable=False)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

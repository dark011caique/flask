from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

# class Jogo():
#     def __init__(self,nome, categoria, console):
#         self.nome = nome
#         self.categoria = categoria
#         self.console = console

# jogo1 = Jogo("Valorante", "FPS", "PC")
# jogo2 = Jogo("LOL", "MMO", "PC")
# jogo3 = Jogo("Free Fire", "MOBA", "Celular")

# lista = [jogo1, jogo2, jogo3]

# class Usuario:
#     def __init__ (self, nome, nickname, senha):
#         self.nome = nome
#         self.nickname = nickname
#         self.senha = senha

# usuario1 = Usuario("Bruno Divino", "BD", "alohomora")
# usuario2 = Usuario("Camila Ferreira", "Mila", "paozinho")
# usuario3 = Usuario("Guilherme Louro", "Cake", "python_eh_vida")

# usuarios = { usuario1.nickname :usuario1, 
#                 usuario2.nickname :usuario2,
#                 usuario3.nickname :usuario3 }

app = Flask(__name__)
app.secret_key = 'alura'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jogoteca.db'
app.config['SECRET_KEY'] = 'secret'

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf =CSRFProtect(app)
bcrypt = Bcrypt(app)

from views_game import *
from views_user import *

if __name__ == '__main__':
    app.run(debug=True)
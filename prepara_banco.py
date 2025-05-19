import sqlite3

print("Conectando ao banco de dados SQLite...")

# Conexão com banco de dados SQLite local (será criado se não existir)
conn = sqlite3.connect('jogoteca.db')
cursor = conn.cursor()

# Apagar tabelas existentes (SQLite não tem DROP DATABASE)
cursor.execute("DROP TABLE IF EXISTS jogos;")
cursor.execute("DROP TABLE IF EXISTS usuarios;")

# Criar tabelas
cursor.execute('''
    CREATE TABLE jogos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        console TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE usuarios (
        nome TEXT NOT NULL,
        nickname TEXT NOT NULL PRIMARY KEY,
        senha TEXT NOT NULL
    );
''')

print("Tabelas criadas com sucesso.")

# Inserir usuários
usuarios = [
    ("Bruno Divino", "BD", "alohomora"),
    ("Camila Ferreira", "Mila", "paozinho"),
    ("Guilherme Louro", "Cake", "python_eh_vida")
]

cursor.executemany('INSERT INTO usuarios (nome, nickname, senha) VALUES (?, ?, ?)', usuarios)

cursor.execute('SELECT * FROM usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# Inserir jogos
jogos = [
    ('Tetris', 'Puzzle', 'Atari'),
    ('God of War', 'Hack n Slash', 'PS2'),
    ('Mortal Kombat', 'Luta', 'PS2'),
    ('Valorant', 'FPS', 'PC'),
    ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
    ('Need for Speed', 'Corrida', 'PS2'),
]

cursor.executemany('INSERT INTO jogos (nome, categoria, console) VALUES (?, ?, ?)', jogos)

cursor.execute('SELECT * FROM jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# Salvar alterações
conn.commit()

cursor.close()
conn.close()

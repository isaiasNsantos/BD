import sqlite3

# 1  -conectando no BD

connection = sqlite3.connect('title.db')

# sempre que for preciso manipular os dados - DDL OU DNL
# 2- Criando UM CURSOR
'''
é um interador que permite navegar e 
manipular os registros em um BD
'''
cursor = connection.cursor()

# 3 - Criando a tabela
cursor.execute('''
    CREATE TABLE movies(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER NOT NULL,
        score REAL NOT NULL
    );
        ''')
# 4 fechando a conexção
print('Tabela criada com secesso')
connection.close()
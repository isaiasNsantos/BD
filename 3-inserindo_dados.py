import sqlite3

# 1  -conectando no BD
connection = sqlite3.connect('title.db')

# sempre que for preciso manipular os dados - DDL OU DNL
# 2- Criando UM CURSOR
'''
Curso é um interador que permite navegar e 
manipular os registros em um BD
'''
cursor = connection.cursor()

# 3 inserindo dados 
cursor.execute('''
    INSERT INTO movies (name, year, score)
    VALUES ("Super Mario", 2023, 10) 
               ''');

cursor.execute('''
    INSERT INTO movies (name, year, score)
    VALUES ("Avatar ", 2023, 9.5) 
               ''');

cursor.execute('''
    INSERT INTO movies (name, year, score)
    VALUES ("Velozes & Furiosos ", 2023, 8.0) 
               ''');
# 4 Gravando Dados no BD

connection.commit()
print('Dados Inseridos com sucesso!')

# 5 fechar a conexão 
connection.close()


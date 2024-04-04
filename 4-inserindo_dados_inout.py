import sqlite3

# 1  -conectando no BD
connection = sqlite3.connect('title.db')
# sempre que for preciso manipular os dados - DDL OU DNL
'''
Curso é um interador que permite navegar e  
manipular os registros em um BD
'''
# 2- Criando UM CURSOR
cursor = connection.cursor()

# 3 solicitando dados do usuario
name = input('Nome do Filme: ')
year = int(input('Ano do filme: '))
score = float(input('Nota do Filme:  '))

# 4 inserindo dados no BD
cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?, ?, ?)
               """, (name, year, score));

# 5 Gravando Dados no BD
connection.commit()
print('Dados Inseridos com sucesso!')

# 6 fechar a conexão 
connection.close()
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

# 3 solicitando dados do usuário
id = int(input('Informe o id do filme que deseja atualizar: '))
name = input('Informa o novo nome do filme: ')

# 4 Atualizando Dados
cursor.execute("""
    UPDATE movies set name = ?
    WHERE id = ?
              """, (name, id))
connection.commit()
print('Dados Inseridos com sucesso!')

# 5 fechar a conexão 
connection.close()
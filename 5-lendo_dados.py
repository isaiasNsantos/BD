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

# 3 Lendo dados da tabela 

data = cursor.execute("""
    SELECT name, year, score FROM movies              
                    """)

print(data.fetchall())# pegando todos os dados da tabela acima 

# 4 Iterando os Dados
for row in cursor.execute('SELECT * FROM movies'):
    print(f'{row}\n')
    
# 5 Ordenando os Dados pelo score
for row in cursor.execute('SELECT * FROM movies ORDER BY score desc'):
    print(f'{row}')
    


# 6 Gravando Dados no BD
connection.commit()
print('Dados Inseridos com sucesso!')

# 7 fechar a conexão 
connection.close()
import sqlite3

# 1  - criando o BD
connection = sqlite3.connect('title.db')
# 2 -Verifica se houve alteração na base de dados
print(connection.total_changes)



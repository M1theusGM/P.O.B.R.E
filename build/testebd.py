import sqlite3

con = sqlite3.connect("cinema.db")

cur = con.cursor()

# cria o BD
'''cur.execute("CREATE TABLE Filme(titulo, ano, duracao)")'''

# Insere dados no BD
'''cur.execute("""
    INSERT INTO Filme VALUES
            ('Star Wars', 1995, 200),
            ('Conan, o Bárbaro', 1982, 129)

""")

con.commit()'''

# mostra todo conteudo do BD
for linha in cur.execute("SELECT ano, titulo FROM Filme ORDER BY ano"):
    print(linha)
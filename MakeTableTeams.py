import sqlite3

# Make Table teams

connection = sqlite3.connect("./Digikaladb.db")
cunsor = connection.cursor()
QUERY = """
        CREATE TABLE teams(
        team_id TINYINT,
        name CHAR(10),
        PRIMARY KEY(team_id) 
        )
"""
cunsor.execute(QUERY)
connection.commit()
connection.close()
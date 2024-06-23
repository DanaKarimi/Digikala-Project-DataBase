import sqlite3

# Make Table employees

connection = sqlite3.connect("./Digikaladb.db")
cunsor = connection.cursor()
QUERY = """
        CREATE TABLE employees(
        id TINYINT,
        name CHAR(10),
        salary INT,
        team_id INT,
        PRIMARY KEY(id),
        FOREIGN KEY (team_id) REFERENCES teams
        )
"""
cunsor.execute(QUERY)
connection.commit()
connection.close()
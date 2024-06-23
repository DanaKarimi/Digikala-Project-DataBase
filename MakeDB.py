import sqlite3
# Make DataBase

connection = sqlite3.connect("./Digikaladb.db")
cunsor = connection.cursor()

QUERY = """

"""
cunsor.execute(QUERY)
connection.commit()
connection.close()
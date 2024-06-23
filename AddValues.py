import sqlite3

# Add VALUES

connection = sqlite3.connect("./Digikaladb.db")
cunsor = connection.cursor()

QUERY = """
        INSERT INTO employees VALUES(1,'Ali',70000,1)
        INSERT INTO employees VALUES(2,'Akbar',90000,1)
        INSERT INTO employees VALUES(3,'Alireza',80000,2)
        INSERT INTO employees VALUES(4,'Bahram',60000,2)
        INSERT INTO employees VALUES(5,'Asghar',90000,1)
        INSERT INTO teams VALUES(1,'Shopping-Operation')
        INSERT INTO teams VALUES(2,'Fulfillment')
        INSERT INTO teams VALUES(3,'Marketplace')
"""
cunsor.execute(QUERY)
connection.commit()
connection.close()
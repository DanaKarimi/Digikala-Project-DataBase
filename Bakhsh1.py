import sqlite3

# Bakhsh1

connection = sqlite3.connect("./Digikaladb.db")
cunsor = connection.cursor()

QUERY = """
        SELECT MAX(salary) FROM employees 
"""

cunsor.execute(QUERY)
results = cunsor.fetchall()
file = open("./Bakhsh1.csv","w")
file.write("salary\n")
for i in results:
    a = str(i[0])
    file.write(a)

file.close()
connection.commit()
connection.close()
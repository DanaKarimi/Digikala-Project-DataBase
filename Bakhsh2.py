import sqlite3

# Bakhsh2

connection = sqlite3.connect("./Digikaladb.db")
cunsor = connection.cursor()

QUERY = """
        SELECT * FROM teams,employees WHERE employees.team_id = teams.team_id
"""
cunsor.execute(QUERY)
results = cunsor.fetchall()
file = open("./Bakhsh2.csv","w")
file.write("team, employee, salary\n")
for i in results:
    if i[4] == 90000 or i[4] == 80000:
        team = i[1]
        employee = i[3]
        salary = str(i[4])
        file.write(team+","+employee+","+salary+"\n")
file.close()
connection.commit()
connection.close()
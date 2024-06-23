import sqlite3


# Make DataBase

# connection = sqlite3.connect("./Digikaladb.db")
# cunsor = connection.cursor()

# QUERY = """

# """
# cunsor.execute(QUERY)
# connection.commit()
# connection.close()



# Make Table employees

# connection = sqlite3.connect("./Digikaladb.db")
# cunsor = connection.cursor()
# QUERY = """
#         CREATE TABLE employees(
#         id TINYINT,
#         name CHAR(10),
#         salary INT,
#         team_id INT,
#         PRIMARY KEY(id),
#         FOREIGN KEY (team_id) REFERENCES teams
#         )
# """
# cunsor.execute(QUERY)
# connection.commit()
# connection.close()



# Make Table teams

# connection = sqlite3.connect("./Digikaladb.db")
# cunsor = connection.cursor()
# QUERY = """
#         CREATE TABLE teams(
#         team_id TINYINT,
#         name CHAR(10),
#         PRIMARY KEY(team_id) 
#         )
# """
# cunsor.execute(QUERY)
# connection.commit()
# connection.close()



# Add VALUES

# connection = sqlite3.connect("./Digikaladb.db")
# cunsor = connection.cursor()

# QUERY = """
#         INSERT INTO employees VALUES(1,'Ali',70000,1)
#         INSERT INTO employees VALUES(2,'Akbar',90000,1)
#         INSERT INTO employees VALUES(3,'Alireza',80000,2)
#         INSERT INTO employees VALUES(4,'Bahram',60000,2)
#         INSERT INTO employees VALUES(5,'Asghar',90000,1)
#         INSERT INTO teams VALUES(1,'Shopping-Operation')
#         INSERT INTO teams VALUES(2,'Fulfillment')
#         INSERT INTO teams VALUES(3,'Marketplace')
# """
# cunsor.execute(QUERY)
# connection.commit()
# connection.close()


# Bakhsh1

# connection = sqlite3.connect("./Digikaladb.db")
# cunsor = connection.cursor()

# QUERY = """
#         SELECT MAX(salary) FROM employees 
# """

# cunsor.execute(QUERY)
# results = cunsor.fetchall()
# file = open("./Bakhsh1.csv","w")
# file.write("salary\n")
# for i in results:
#     a = str(i[0])
#     file.write(a)

# file.close()
# connection.commit()
# connection.close()



# Bakhsh2

# connection = sqlite3.connect("./Digikaladb.db")
# cunsor = connection.cursor()

# QUERY = """
#         SELECT * FROM teams,employees WHERE employees.team_id = teams.team_id
# """
# cunsor.execute(QUERY)
# results = cunsor.fetchall()
# file = open("./Bakhsh2.csv","w")
# file.write("team, employee, salary\n")
# for i in results:
#     if i[4] == 90000 or i[4] == 80000:
#         team = i[1]
#         employee = i[3]
#         salary = str(i[4])
#         file.write(team+","+employee+","+salary+"\n")
# file.close()
# connection.commit()
# connection.close()




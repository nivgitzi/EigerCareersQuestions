import mysql.connector

eigerQuestion2DB = mysql.connector.connect(host='localhost', user='root', password='12345', database='EigerQuestion2Database')

mycursor = eigerQuestion2DB.cursor()

# mycursor.execute("CREATE DATABASE EigerQuestion2Database")   # needed this line for creating the database
                                                               # once the database is created, we no longer need it

# Create DEPARTMENT table
mycursor.execute("CREATE TABLE DEPARTMENT (ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, NAME VARCHAR(255), LOCATION VARCHAR(255))")

# Create EMPLOYEE table
mycursor.execute("CREATE TABLE EMPLOYEE (ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, NAME VARCHAR(255), SALARY INT, DEPT_ID INT, FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT(ID))")



# Insert data into DEPARTMENT table
mycursor.execute("INSERT INTO DEPARTMENT (NAME, LOCATION) VALUES ('Executive','Sydney')")
mycursor.execute("INSERT INTO DEPARTMENT (NAME, LOCATION) VALUES ('Production','Sydney')")
mycursor.execute("INSERT INTO DEPARTMENT (NAME, LOCATION) VALUES ('Resources','Cape Town')")
mycursor.execute("INSERT INTO DEPARTMENT (NAME, LOCATION) VALUES ('Technical','Texas')")
mycursor.execute("INSERT INTO DEPARTMENT (NAME, LOCATION) VALUES ('Management','Paris')")
# Insert data into EMPLOYEE table
mycursor.execute("INSERT INTO EMPLOYEE (NAME, SALARY, DEPT_ID) VALUES ('Candice', 4685, 1)")
mycursor.execute("INSERT INTO EMPLOYEE (NAME, SALARY, DEPT_ID) VALUES ('Julia', 2559, 2)")
mycursor.execute("INSERT INTO EMPLOYEE (NAME, SALARY, DEPT_ID) VALUES ('Bob', 4405, 4)")
mycursor.execute("INSERT INTO EMPLOYEE (NAME, SALARY, DEPT_ID) VALUES ('Scarlet', 2350, 1)")
mycursor.execute("INSERT INTO EMPLOYEE (NAME, SALARY, DEPT_ID) VALUES ('Ileana', 1151, 4)")


eigerQuestion2DB.commit()


# query which generates the number of employees in each department
mycursor.execute("SELECT DEPARTMENT.NAME as 'DepartmentName', COUNT(EMPLOYEE.ID) as 'AmountOfEmployees' FROM EMPLOYEE RIGHT JOIN DEPARTMENT ON EMPLOYEE.DEPT_ID = DEPARTMENT.ID GROUP BY DEPARTMENT.NAME ORDER BY COUNT(EMPLOYEE.ID) DESC, DEPARTMENT.NAME ASC")


# Print results
print("'DepartmentName' | 'AmountOfEmployees'")
for row in mycursor:
    print(row)


mycursor.close()
eigerQuestion2DB.close()

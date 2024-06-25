
# SETUP VIRTUAL ENVIRONMENT
# 1. Create Virtual Env
# python -m venv myenv

# 2. Activate Virtual Env
#.\myenv\Scripts\activate

# 3. Installation of Driver
# pip install mysql-connector-python


# Database Connection
import mysql.connector as db

from Session14a import employee

# Database username and password
# username = "root"
# password = "0811"

# # Local Host
# host = "127.0.0.1"
# database = "training"

# connection = db.connect(user = username, password = password, host = host, database= database)

connection = db.connect(user = "root", password = "0811", host ="127.0.0.1", database= "training")
print("Connection created")
print(connection)

employee1 = employee()
employee1.add_details()

# Create SQL Statement
# Hard Coding
#sql = "insert into employee values(null, 'Navkiran', 20, 'Designing', 'Team Head', 50000)"

# To have inputs from user
sql = "insert into employee values(null, '{}', {}, '{}', '{}', '{}')".format(employee1.name, employee1.age, employee1.field,employee1.position,employee1.salary)

# Updating data
#sql_update = "update employee set salary = 70000 where name = 'mayank'"

# Deleting data 
#sql_delete = " delete from employee where cid = 3"
# Obtain Cursor -> Perform CRUD operations with MySQL
cursor = connection.cursor()

# Execute SQL Command
cursor.execute(sql)
#cursor.execute(sql_update)
#cursor.execute(sql_delete)

# Commit the Write Operation
connection.commit()

print("SQL Statement Executed..")
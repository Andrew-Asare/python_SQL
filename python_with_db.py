# To establish connection between python and SQL we will use PYODBC

import pyodbc

# Let's establish the connection using PYODBC
server = "18.135.103.95"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Let's check if the connection is validated and cursor object is created
cursor = docker_Northwind.cursor()
print(cursor.execute("SELECT @@version;"))

# Let's fetch some data from Northwind DB

raw = cursor.fetchone()
print(raw)

# Let's connect to our DB and fetch some data from Customers table
cust_rows = cursor.execute("SELECT * FROM Customers").fetchall
print(cust_rows)
# We use execute to run our quires with in a string
# fetchall() gets all the data from the table

prod_rows = cursor.execute("SELECT * FROM Products").fetchall()
# Let's iterate through the Product Table and check the UnitPrice available
for records in prod_rows:
    print(records.UnitPrice)

row = cursor.execute("SELECT *  FROM Products")
while True:
    records = row.fetchone()
    if records is None:
        break
    print(records.UnitPrice)













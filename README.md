
# Python with SQL
## Establishing a connection with PYODBC
## Apply CRUD 
### Making data persistent


![SQL, Python](https://user-images.githubusercontent.com/26543682/112972756-82057280-9148-11eb-8d2e-22544df39c81.png)


- Use `pip install pyodbc`
```python
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
```

# SQL TASK 
```
# SQL OOP

## Timings

25 - 30

* OOP example using pyodbc

create an example of how we can create service objects related to a particular table.

## An sql manager for the products table

create an object that relates only to the products table in the Northwind database. The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.

As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department. 

The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions within a single object.

Create two files `nw_products.py` & `nw_runner.py` and then we will move into creating our object.

APPLY OOP - DRY CRUD WHERE POSSIBLE
```


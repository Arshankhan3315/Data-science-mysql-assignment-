#Question-1. What is a database? Differentiate between SQL and NoSQL databases.
"""answer-1-
A database is a structured collection of data that is organized in a way that allows efficient storage, retrieval
 and management of information. It can store a wide range of data types, including text, numbers, images, and more.
  Databases are crucial for various applications and systems to handle large amounts of data and enable efficient data querying
   and manipulation."""
#SQL (Relational) Databases:
#SQL databases are based on the relational model and use a structured query language (SQL) 
# for defining and manipulating the data. They organize data into tables,
#  where each table has predefined columns and data types.
#Examples of SQL databases:
#1-MySQL
#2-PostgreSQL
#3-Oracle
#4-Microsoft SQL Server
#NoSQL Databases:
"""NoSQL databases, as the name suggests, do not use SQL for querying and managing data.
 They are designed to handle unstructured or semi-structured data and provide more flexible and scalable options 
 for data storage and retrieval.
  NoSQL databases are suitable for handling large volumes of data and are often used in web applications and big data processing."""
#Examples of NoSQL databases:
#1-MongoDB (document-based)
#2-Cassandra (wide-column)
#3-Redis (key-value)
#4-Neo4j (graph)
#Question-2. What is DDL? Explain why CREATE, DROP, ALTER, and TRUNCATE are used with an example.
"""answer-2-DDL (Data Definition Language):
 DDL is a subset of SQL (Structured Query Language) used to define the structure and schema of the database.
  It includes commands for creating, modifying, and deleting database objects like tables, indexes, views, and schemas.
   DDL statements have a significant impact on the database structure and require appropriate permissions to execute."""


#create database
import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists company")
mydb.close()

#create table
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if not exists company.Employees(Employees_id INT, FirstName VARCHAR(50),LastName VARCHAR(50), Department VARCHAR(50))")
mydb.close()


#insert values
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into company.Employees values(01, 'arshan', 'khan', 'datascience',0000)")
mycursor.execute("insert into company.Employees values(02, 'ayan', 'khan', 'doctor',000)");
mydb.commit()
mydb.close()

#drop 
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
  database="company"
)
mycursor = mydb.cursor()
delete_query = "DELETE FROM Employees WHERE FirstName='ayan'"
mycursor.execute(delete_query)
mydb.commit()
mydb.close()

#Alter table
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
  database="company"
)
mycursor = mydb.cursor()
mycursor.execute("alter table Employees add bSalary INT(10)")
mydb.commit()
mydb.close()


#TRUNCATE
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
  database="company"
)
mycursor = mydb.cursor()
mycursor.execute("TRUNCATE TABLE Employees ") 
mydb.commit()
mydb.close()

#Question-3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
#answer-3-
# """DML, or Data Manipulation Language, is a subset of SQL (Structured Query Language) used to manage
#  and manipulate data within relational databases.
#  DML consists of three main operations: INSERT, UPDATE, and DELETE, which are used to add, modify, and remove data, respectively."""

#insert values
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into company.Employees values(01, 'arshan', 'khan', 'datascience',0000)")
mycursor.execute("insert into company.Employees values(02, 'ayan', 'khan', 'doctor',000)");
mydb.commit()
mydb.close()

#update 
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
  database="company"
)
mycursor = mydb.cursor()
mycursor.execute("UPDATE Employees SET FirstName='updated FirstName' WHERE FirstName='ayan'")
mydb.commit()
mydb.close()

#delete
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
  database="company"
)
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM Employees WHERE FirstName='updated FirstName'")
mydb.commit()
mydb.close()


#Question-4. What is DQL? Explain SELECT with an example.
#answer-4-"""DQL, or Data Query Language, is a subset of SQL (Structured Query Language) used to retrieve and query data
#  from a database. The primary statement in DQL is SELECT,
#  which is used to retrieve data from one or more tables based on specified criteria"""

#example
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("select * from company.Employees")
for i in mycursor.fetchall():
  print(i)
mydb.close()

#Q5. Explain Primary Key and Foreign Key.
#answer-5-Primary Key:

"""A primary key is a special type of unique identifier within a relational database.
 It uniquely identifies each record or row in a table and ensures that each record has a unique value for the primary key column.
  Primary keys play a crucial role in maintaining data integrity and establishing relationships between tables."""

#Foreign Key:

"""A foreign key is a field or a set of fields in a table that refers to the primary key of another table.
 It establishes a relationship between two tables, known as the parent table (the table with the primary key)
  and the child table (the table with the foreign key). Foreign keys help maintain referential integrity,
   ensuring that relationships between tables remain consistent and valid. Key points about foreign keys are:"""


#Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
#answer-6-"""To connect to MySQL from Python, you'll need a MySQL Python connector like mysql-connector-python.
#  Below is a Python code that demonstrates how to connect to MySQL and use the cursor() and execute() methods:"""
#explain

#mysql.connector.connect(**config): Establishes a connection to the MySQL database using the provided configuration.

#connection.cursor(): Creates a cursor object associated with the connection. A cursor allows you to execute SQL statements and fetch data.

#cursor.execute(query): Executes the SQL query specified by query.

#cursor.fetchall(): Fetches all the rows resulting from the executed query.

#Finally, we close the cursor and the connection to release resources once the required operations are completed.


import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("select * from company.Employees")
for i in mycursor.fetchall():
  print(i)
mydb.close()

#Q7. Give the order of execution of SQL clauses in an SQL query.
#answer-7-
"""In a typical SQL query, the clauses are executed in a specific order, 
although they might not always appear in this order in the actual SQL statement. The general order of execution is as follows"""

#FROM: The FROM clause identifies the tables or views from which the data will be retrieved.

#WHERE: The WHERE clause filters the rows based on specified conditions, restricting the result set.

#GROUP BY: The GROUP BY clause groups rows that have the same values into summary rows, often used with aggregate functions like COUNT, SUM, AVG, etc.

#HAVING: The HAVING clause filters the result set based on conditions specified after the GROUP BY clause.

#SELECT: The SELECT clause determines the columns to be retrieved from the tables.

#ORDER BY: The ORDER BY clause sorts the result set based on specified column(s) and sort order.

#LIMIT/OFFSET (optional): The LIMIT clause limits the number of rows returned, and the OFFSET clause sets where to begin the result set.

#assignment completed








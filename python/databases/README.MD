## Databases 
= a structured collection of data that is organized and managed in a way that allows efficient manipulation
(CRUD)
= data is typically organized into tables 
= tables consists of rows and columns 

id |  name | staffid
1     joseph  1

= each row represents a record or entry
= each column represents a specific attribute about that record  

## Types of databases 
1. Relational Databases : (RDBMS) : these dbs organize data into tables with rows and columns and establishes 
relationships between the tables using keys.(primary or forieng keys.)
SQL : these dbs use the structured query language for querying and manipulating data. 

MySQL , PostgreSQL , Oracle DB , SQLite

2. NoSQL Databases : non-relational databases , they simply store unstructured, semi-structured or structured data. 
Firebase (HTML ,CSS , JS) , MongoDB , Cassandra  

3. Document Databases : Store data in a semi-structured manner typically using JSON, BSON , XML 
Firebase , MongoDB, CouchDB 


## Fundamentals when designing a database 
1. Identify requirements 
2. Conceptual Design : use of ER diagrams to model the relationships. 
3. Normalize data: SSOT
4. Choice of data type : select the right data type for the attributes (columns) based on the nature of the data 
and its storage requirements : 
5. Define Keys : identify the Primary key (ID (A.I)) and foreign keys to establish the relationships between the tables 
6. Review and Iterate 
7. Document the design : dbdiagram.io


## SQLite 
Its a lightweight and self-contained SQL DB engine , embedded directly into applications. 
Python already has sqlite3. 

1. Import the sqlite3 module : import sqlite3
2. Connect to the database 
3. Create a cursor object : this object allows us to execute our sql queries 
4. Execute the queries 
5. Commit the changes to the db 
6. Close the connection .
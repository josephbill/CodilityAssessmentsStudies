'''
SQL Joins are operations that allow you to combine rows from two or more tables based on a related column 
Joins enable querying and retrieving data across multiple tables. 

1. Inner Join 
: returns only the rows that have matching values in both tables involved in the join statement  
: The syntax has a condition which determines which rows from each table are combined 
: If no match for a row in one of the tables that row is not included in the result 

'SELECT * FROM table1 INNER JOIN table2 ON table1.column = table2.column;' : result = records from table1.

2. LEFT JOIN (or LEFT OUTER JOIN)
: returns all the rows from the left table and matching rows from the right table 
: if no match for the right table, Null values are used for the columns from that table 

'SELECT * FROM table1 LEFT JOIN table2 ON table1.column = table2.column'

3. RIGHT JOIN (or RIGHT OUTER JOIN)
: returns all the rows from the right table and matching rows from the left table 
: if no match for the left table, Null values are used for the columns from that table 

'SELECT * FROM table1 RIGHT JOIN table2 ON table1.column = table2.column'

4. FULL JOIN (or FULL OUTER JOIN)
: returns all rows from both tables and matches rows where possible 
: if no match for a row in one of the tables , Null values are used for the columns from that table 


'SELECT * FROM table1 FULL JOIN table2 on table1.column = table2.column'

'''
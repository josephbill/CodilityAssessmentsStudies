'''
ORM (This is simply a technique used to interact with a relational DB using an OOP language like Python)

Allows us to work with database entities (tables _> columns, rows) as Python objects 
1. Simplifies the db operations 
2. Makes code more readable and maintainable  
SQL Engines -> MYSQL , SQLITE , POSTGRESQL 
FLASK -> Library efficient ORM 
'''
import sqlite3

'''
I want a products table 
- name 
- price 

Tables  === classes 
Tables Columns  === Attributes / Properties 
Tables rows === Object instances 

'''

class Product:
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    def __init__(self, id, name , price) -> None:
        self.id = id 
        self.name = name
        self.price = price 

    # create several methods that relate class 
    def save(self):
        Product.cursor.execute('INSERT INTO products (id, name, price) VALUES (?,?,?)', (self.id,self.name,self.price))
        Product.conn.commit()
        Product.conn.close()


# creating the products table 
def create_table():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT , price INTEGER);
''')
    conn.commit()
    conn.close()


create_table()
# creating the objects 
new_product = Product(1, 'Laptop', 999)
# call methods from my class 
new_product.save()
    

    


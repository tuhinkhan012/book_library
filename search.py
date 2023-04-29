import mysql

conn = mysql.connect('library.db')
c = conn.cursor()

def view_books():
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    for row in rows:
        print(row)

def search_books(name=None, name of publisher=None, date of publisher=None, type=None):
    query = "SELECT * FROM books WHERE 1=1"
    if name:
        query += " AND name LIKE ?"
    if name of publisher:
        query += " AND name of publisher LIKE ?"
    if age:
        query += " AND age = ?"
    if date of publisher:
        query += " AND date of publisher = ?"
    if type:
        query += " AND type LIKE = ?"
 
    c.execute(query, ('%'+name+'%', '%'+name of publication+'%', '%'+age+'%', '%'+date of publisher+'%', type))
    rows = c.fetchall()
    for row in rows:
        print(row)

view_books()

name = input("Enter title to search (leave blank to skip): ")
name of publisher = input("Enter name of publisher to search (leave blank to skip): ")
age = input("Enter age to search (leave blank to skip): ")
date of publication = input("Enter date of publication to search (leave blank to skip): ")
type = input("Enter type to search (leave blank to skip): ")

search_books(name, name of publisher, age, date of publication, type)

conn.close()

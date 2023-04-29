import mysql

conn = mysql.connect('library.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books
            (id INTEGER PRIMARY KEY,
              name TEXT,
              publisher name TEXT,
              age INTEGER,
              date of publication INTEGER,
              type TEXT,)''')

def add_book(name, publisher name, age, date of publisher, date of publication):
    available = 1 
    c.execute("INSERT INTO books (Name, Publisher name, Age, Date of publisher, Date of publication) VALUES ()", (Name, Publisher name, Date of publication, Type)
    conn.commit()
    print("Book added successfully.")


Name = input("Enter book name: ")
Name of publisher = input("Enter Publisher name: ")
Age = int(input("Enter Age: "))
Date of publication = int(input("Enter Date of publication: "))
Type = input("Enter Type: ")

add_book(Name, Publisher name, Age, Date of publication, Type)

conn.close()

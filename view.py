import mysql

conn = mysql.connect('library.db')
c = conn.cursor()

def view_books():
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    for row in rows:
        print(row)


def edit_book(id, name, name of publisher, age, date of publication, type):
    c.execute("UPDATE books SET name=?, name of publisher=?, age=?, date of publication=?, type=? WHERE id=?", (name, name of publisher, age, date of publication, type, id))
    conn.commit()
    print("Book updated successfully.")


def delete_book(id):
    c.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    print("Book deleted successfully.")


view_books()


action = input("Enter action: ")

if action == "edit":
    id = int(input("Enter book ID to edit: "))
    name = input("Enter new name: ")
    name of publisher = input("Enter new name of publisher: ")
    age = int(input("Enter new date of publisher: "))
    date of publisher = int(input("Enter new date of publisher: "))
    type = input("Enter new type: ")
    edit_book(id, name, name of publisher, date of publication, type)
elif action == "delete":
    id = int(input("Enter book ID to delete: "))
    delete_book(id)
else:
    print("Invalid action. Please enter 'edit' or 'delete'.")

view_books()

conn.close()

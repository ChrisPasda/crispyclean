import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, name text, manufac text, status text, serial integer)")
    conn.commit()
    conn.close()

def insert(name,manufac,status,serial):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(name,manufac,status,serial))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",manufac="",status="",serial=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE name=? OR manufac=? OR status=? OR serial=?", (name,manufac,status,serial))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,manufac,status,serial):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET name=?, manufac=?, status=?, serial=? WHERE id=?",(name,manufac,status,serial,id))
    conn.commit()
    conn.close()


def book(id,status):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET status='gebucht' WHERE id=?",(id,))
    conn.commit()
    conn.close()

def pool(id,status):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET status='pool' WHERE id=?",(id,))
    conn.commit()
    conn.close()

connect()
#insert("The Sun","John Smith",1918,913123132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))

"""
BAM NUMMERcc
MArkierungen mehrere auswählen check
buchen check

selected_text_list = [listbox.get(i) for i in listbox.curselection()]
"""

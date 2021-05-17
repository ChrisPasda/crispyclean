import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, name text, manufac text, status text, serial integer, bam integer)")
    conn.commit()
    conn.close()

def insert(name,manufac,status,serial,bam):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?)",(name,manufac,status,serial,bam))
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

def search(name="",manufac="",status="",serial="",bam=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE name=? OR manufac=? OR status=? OR serial=? OR bam=?", (name,manufac,status,serial,bam))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,manufac,status,serial,bam):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET name=?, manufac=?, status=?, serial=?,bam=? WHERE id=?",(name,manufac,status,serial,bam,id))
    conn.commit()
    conn.close()

def updateBam(id,bam):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET bam=? WHERE id=?", (bam,id))
    conn.commit()
    conn.close()

def deleateBam(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET bam='' WHERE id=?", (id,))
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

def checkStatus(name="",manufac="",status="",serial="",bam=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE name=? OR manufac=? OR status != 'gebucht' OR serial=? OR bam=?", (name,manufac,serial,bam))
    rows=cur.fetchall()
    conn.close()
    return rows

connect()


"""
ZUTUN:

search bam einzeln, damit name usw nicht kollidieren
check status danach bam als eigene liste gebuchter laptops erstellen und in gui anzeigen am besten



"""

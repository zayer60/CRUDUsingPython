import sqlite3


class Database:

    def __init__(self, db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS student(regid INTEGER PRIMARY KEY,roll INTEGER,name TEXT,dob INTEGER,gender TEXT)")
        conn.commit()
        conn.close()

    def insert(self, roll, name, dob, gender):
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO student VALUES(NULL,?,?,?,?)", (roll, name, dob, gender))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, roll="", name="", dob="", gender=""):
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM student WHERE roll =? OR name =? OR dob =? OR gender =?", (roll, name, dob, gender))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, regid):
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM student where regid =?", (regid,))
        conn.commit()
        conn.close()

    def update(self, regid, roll, name, dob, gender):
        conn = sqlite3.connect("students.db")
        cur = conn.cursor()
        cur.execute("UPDATE student SET roll =?,name=?,dob=?,gender=? WHERE regid=?", (roll, name, dob, gender, regid))
        conn.commit()
        conn.close()


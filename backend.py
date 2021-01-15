import sqlite3


def connect():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS student(regid INTEGER PRIMARY KEY,roll INTEGER,name TEXT,dob INTEGER,gender TEXT)")
    conn.commit()
    conn.close()


def insert(roll, name, dob, gender):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO student VALUES(NULL,?,?,?,?)", (roll, name, dob, gender))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(roll="", name="", dob="", gender=""):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE roll =? OR name =? OR dob =? OR gender =?", (roll, name, dob, gender))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(regid):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student where regid =?", (regid,))
    conn.commit()
    conn.close()


def update(regid, roll, name, dob, gender):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET roll =?,name=?,dob=?,gender=? WHERE regid=?", (roll, name, dob, gender, regid))
    conn.commit()
    conn.close()


connect()

print(view())


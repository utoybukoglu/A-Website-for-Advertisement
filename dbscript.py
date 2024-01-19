import sqlite3

def createDatabase(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS USER("
              "username TEXT PRIMARY KEY,"
              "password TEXT,"
              "fullname TEXT,"
              "email TEXT,"
              "telno TEXT)")

    c.execute("CREATE TABLE IF NOT EXISTS CATEGORY("
              "cid INTEGER PRIMARY KEY AUTOINCREMENT,"
              "cname TEXT)")

    c.execute("CREATE TABLE IF NOT EXISTS ADVERTISEMENT("
              "aid INTEGER PRIMARY KEY AUTOINCREMENT,"
              "title TEXT,"
              "description TEXT,"
              "isactive TEXT,"
              "username TEXT,"
              "cid INTEGER,"
              "FOREIGN KEY (username) REFERENCES USER(username),"
              "FOREIGN KEY (cid) REFERENCES CATEGORY(cid))")

    conn.commit()
    conn.close()

def insert_categories(dbname, categories):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    for cname in categories.values():
        c.execute("INSERT INTO CATEGORY (cname) VALUES (?)", (cname,))
    conn.commit()
    conn.close()

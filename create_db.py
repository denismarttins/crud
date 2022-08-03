import sqlite3 as sql

con = sql.connect('db_web.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS users')

sql = '''CREATE TABLE "users" (
    "UID" INTEGER PRIMARY KEY AUTOINCREMENT,
    "UNAME" TEXT,
    "PROCESSO" TEXT,
    "CASO" TEXT,
    "ANDAMENTO" TEXT
    )'''

cur.execute(sql)
con.commit()
con.close()
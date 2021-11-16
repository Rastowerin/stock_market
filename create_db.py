import sqlite3

con = sqlite3.connect('companies.db')
cur = con.cursor()

cur.execute("CREATE TABLE companies ("
            "name STRING NOT NULL,"
            "c2018 INTEGER NOT NULL,"
            "c2019 INTEGER NOT NULL,"
            "cap INTEGER NOT NULL"
            ")")

import sqlite3

con = sqlite3.connect('companies.db')
cur = con.cursor()

cur.execute("DROP TABLE companies")

s = ''
for year in range(2006, 2022):
    s += "c{} INTEGER,".format(year)

cur.execute("CREATE TABLE companies ("
            "name STRING NOT NULL,"
            "{}"
            "cap INTEGER NOT NULL"
            ")".format(s))

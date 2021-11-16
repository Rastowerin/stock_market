import requests
import sqlite3
import company


url = r'https://iss.moex.com/iss/engines/stock/markets/shares/boardgroups/57/securities.jsonp?' \
      r'iss.meta=off&iss.json=extended&security_collection=3&sort_column=SHORTNAME&sort_order=asc&lang=ru&_=1637073879814'

r = requests.get(url)
h = r.json()[1]['securities']
h = h[::-1]
r.close()

for i in range(len(h)):

      comp = company.Company(h[i]['SECID'])

      con = sqlite3.connect('companies.db')
      cur = con.cursor()

      cur.execute("SELECT * FROM companies WHERE name == '{}'".format(str(comp)))

      if comp and len(cur.fetchall()) == 0:
            comp.load()
      print(comp.get_name(), i + 1)

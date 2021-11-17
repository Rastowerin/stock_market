import requests
import sqlite3
import company
import func


url = r'https://iss.moex.com/iss/engines/stock/markets/shares/boardgroups/57/securities.jsonp?' \
      r'iss.meta=off&iss.json=extended&security_collection=3&sort_column=SHORTNAME&sort_order=asc&lang=ru&_=1637073879814'

r = requests.get(url)
h = r.json()[1]['securities']
h = h[::-1]
r.close()

for i in range(len(h)):

      comp = func.get_info(h[i]['SECID'])

      if not comp:
            continue

      con = sqlite3.connect('companies.db')
      cur = con.cursor()

      cur.execute("SELECT * FROM companies WHERE name == '{}'".format(comp[0]))

      if comp and len(cur.fetchall()) == 0:

            s1, s2 = '', ''
            for year in range(2006, 2022):
                  s1 += 'c{}, '.format(year)
                  s2 += "'{}', ".format(comp[1][year])

            cur.execute("INSERT INTO companies(name, {}cap) VALUES ('{}', {}{})".format(s1, comp[0], s2, comp[2]))
            con.commit()

      print(comp[0], i + 1)

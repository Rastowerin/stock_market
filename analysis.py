import matplotlib.pyplot as plt
import sqlite3
import company
import func

con = sqlite3.connect('companies.db')
cur = con.cursor()

cur.execute("SELECT * FROM companies")

companies_list = list(map(lambda x: company.Company(*x), cur.fetchall()))
companies_list.sort()

indicators, caps = [], []
for i in range(len(companies_list)):

    company = companies_list[i]
    indicator = max(company.get_c2018() / company.get_c2019(), company.get_c2019() / company.get_c2018())

    indicators.append(indicator)
    caps.append(company.get_cap())

indicators = func.average_array(indicators, 50)

plt.plot(caps, indicators)
plt.show()

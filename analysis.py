import matplotlib.pyplot as plt
import sqlite3
import company
import func

con = sqlite3.connect('companies.db')
cur = con.cursor()

cur.execute("SELECT * FROM companies")

companies_list = cur.fetchall()
for i in range(len(companies_list)):
    cost_dict = {year: companies_list[i][1 + year - 2006] for year in range(2006, 2022)}
    companies_list[i] = [companies_list[i][0], cost_dict, companies_list[i][-1]]

companies_list = list(map(lambda x: company.Company(*x), companies_list))
companies_list.sort()

change_factors, caps = [], []
for i in range(len(companies_list)):

    company = companies_list[i]

    for year in range(2006, 2022):

        change_factor = company.get_change_factor_in_year(year)

        if change_factor is None or change_factor > 20:
            continue

        change_factors.append(change_factor)
        caps.append(len(caps) + 1)
        # caps.append(company.get_cap())

indicators = func.average_array(change_factors, 100)

plt.plot(caps, indicators)
plt.show()

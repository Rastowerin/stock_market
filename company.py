import sqlite3
import func


class Company:

    def __init__(self, name):

        self.name = name
        data = func.get_info(name)

        f = True
        con = sqlite3.connect('companies.db')
        cur = con.cursor()

        if data:
            self.c2018, self.c2019, self.cap = func.get_info(name)
        else:
            self.c2018, self.c2019, self.cap = None, None, None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.cap < other.cap

    def __le__(self, other):
        return self.cap - other.cap

    def __eq__(self, other):
        return self.cap == other.cap

    def __ne__(self, other):
        return self.cap != other.cap

    def __gt__(self, other):
        return self.cap > other.cap

    def __ge__(self, other):
        return self.cap >= other.cap

    def __bool__(self):
        return bool(self.cap)

    def get_name(self):
        return self.name

    def load(self):

        con = sqlite3.connect('companies.db')
        cur = con.cursor()

        cur.execute("INSERT INTO companies(name, c2018, c2019, cap) VALUES ('{}', {}, {}, {})".format(
            self.name, self.c2018, self.c2019, self.cap))
        con.commit()

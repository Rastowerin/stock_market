import sqlite3


class Company:

    def __init__(self, name, c2018, c2019, cap):

        self.name = name

        if None not in (c2018, c2019, cap):
            self.c2018, self.c2019, self.cap = c2018, c2019, cap
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

    def get_c2018(self):
        return self.c2018

    def get_c2019(self):
        return self.c2019

    def get_cap(self):
        return self.cap

    def load(self):

        con = sqlite3.connect('companies.db')
        cur = con.cursor()

        cur.execute("INSERT INTO companies(name, c2018, c2019, cap) VALUES ('{}', {}, {}, {})".format(
            self.name, self.c2018, self.c2019, self.cap))
        con.commit()

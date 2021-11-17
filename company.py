import sqlite3


class Company:

    def __init__(self, name, cost_dict, cap):

        self.name, self.cost_dict, self.cap = name, cost_dict, cap

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

    def get_cost_in_year(self, year):
        return self.cost_dict[year]

    def get_change_factor_in_year(self, year):

        if self.cost_dict[year] != 'None' and (year + 1) in self.cost_dict.keys() and self.cost_dict[year + 1] != 'None':
            return max(float(self.cost_dict[year]) / float(self.cost_dict[year + 1]),
                       float(self.cost_dict[year + 1]) / float(self.cost_dict[year]))

        return None

    def get_cap(self):
        return self.cap

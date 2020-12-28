import datetime

class Worker:
    def __init__(self, surname_initials, born_date, hiring_date, salary_amount):
        self.surname_initials = surname_initials
        self.born_date = datetime.datetime(*born_date)
        self.hiring_date = datetime.datetime(*hiring_date)
        self.salary_amount = salary_amount

    def expirience(self):
        exp = datetime.datetime.today() - self.hiring_date
        exp_h = exp.total_seconds() // 3600
        exp_y = exp_h // 8760
        exp_m = (exp_h % 8760) // 730
        return (exp_y, exp_m)

    def age(self):
        age = datetime.datetime.today() - self.born_date
        age_h = age.total_seconds() // 3600
        return  age_h // 8760

    def salery_sum(self):
        y, m = self.experience()
        return ((y * 12) + m) * self.salary_amount
#y = years
#h = hours
#m = mounth
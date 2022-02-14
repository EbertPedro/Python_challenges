class employee:
    
    num_of_emps = 0
    # raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        employee.num_of_emps += 1
    
    def fullname(self):
        return "My full name is: {0:s} {1:s}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
        
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = employee("Corey", "schafer", 50000)
emp2 = employee("Test", "user", 60000)

import datetime
my_date = datetime.date(2016,7,8)
is_date_to_work = employee.is_workday(my_date)

if is_date_to_work == False:
    print("Today is free day :))")
else:
    print("Today is time of work :((")
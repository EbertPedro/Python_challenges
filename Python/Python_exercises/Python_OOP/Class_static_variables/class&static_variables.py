class employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        employee.num_of_emps += 1
    
    def fullname(self):
        return "My full name is: {0:s} {1:s}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = employee("Corey", "schafer", 50000)
emp2 = employee("Test", "user", 60000)

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

# emp1.raise_amount = 1.05
# print(employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# print(emp1.__dict__)
# print(employee.__dict__)
# print(id(emp1.raise_amount))
# print(id(employee.raise_amount))

print(employee.num_of_emps)
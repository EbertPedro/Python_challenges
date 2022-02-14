class employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    
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

emp1 = employee("Corey", "schafer", 50000)
emp2 = employee("Test", "user", 60000)

print(employee.__dict__)  #variables to class employee before change the values by @classmethod 
employee.set_raise_amt(1.05) #change the class variable(attribute) raise_amt 
 
print(employee.raise_amt) #checking the values have changed to employee, emp1, emp2
print(emp1.raise_amt)
print(emp2.raise_amt)

print(emp1.__dict__)
print(employee.__dict__) #variables to class employee after change the values by @classmethod 
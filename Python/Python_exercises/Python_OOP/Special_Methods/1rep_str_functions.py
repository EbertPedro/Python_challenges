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
        
    def __repr__(self):
        # pass
        return "Employee('{}, {}, {}')".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
        
emp1 = employee("Corey", "schafer", 50000)
emp2 = employee("Test", "name", 60000)

print(emp1.__repr__())  #as same as print(repr(emp1))
print(emp1.__str__())   #as same as print(str(emp1))
print(emp1)
# print(emp1.__dict__)
# print(help(emp1))

# print(dir(int))
print(int.__add__(1,2))
# print(int.__str__(1))
# print(float.__repr__(1.0))
# print(isinstance(1,int))
#print(issubclass(1,int))
print(help(int))
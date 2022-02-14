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

class Developer(employee):
    # raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
        
dev1 = Developer("Corey", "schafer", 50000, "Python")
# dev2 = Developer("Test", "user", 60000, "Java")

# print(help(employee))
# print(help(Developer))

# dev1.raise_amt = 1.30
print(dev1.email)
print(dev1.prog_lang)
print(help(dev1))
print(dev1.__dict__)
print(dev1.num_of_emps)
print(dev1.raise_amt)
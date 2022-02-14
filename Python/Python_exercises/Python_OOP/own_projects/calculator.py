"""
This class enployee set the attribuites first and last name 
and was setted the attribuites email and full name to change 
set dinamic by the decorators @property, @name.setter and 
@name.deleter. With this class we can change dinamicly the 
attribuites that can be chanching whit others users.
"""

class calculator:
    
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        calculator.num_of_emps += 1
    
    def fullname(self):
        return "My full name is: {0:s} {1:s}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
dev1 = calculator("Corey", "schafer", 50000, "Python")
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
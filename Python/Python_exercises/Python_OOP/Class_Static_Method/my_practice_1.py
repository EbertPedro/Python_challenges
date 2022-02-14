class employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    rate_desc = 0.95    
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
    
    def apply_desc(self):
        self.desc = self.pay * employee.rate_desc

    @classmethod
    def change_rate_desc(cls,new_rate_desc):
        cls.rate_desc = new_rate_desc
        
    @staticmethod
    def get_password(last_digite):
        # return "The password obtained is: {0:f}".format(employee.rate_desc*last_digite)
        employee.rate_desc = last_digite

dev1 = employee("Corey", "schafer", 10000)
# dev2 = Developer("Test", "user", 60000)
# print(dev1.email)
# dev1.apply_desc()
# print(dev1.desc)

print(employee.rate_desc)
employee.change_rate_desc(0.96)
print(employee.rate_desc)

print(dev1.__dict__)
dev1.change_rate_desc(0.98)
print(dev1.__dict__)
print(employee.rate_desc)

employee.get_password(2)
print(employee.rate_desc)

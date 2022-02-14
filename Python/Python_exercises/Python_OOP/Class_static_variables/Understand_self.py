class employee:
    
    var_inner = "discovery..."
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return "My full name is: {0:s} {1:s}".format(self.first, self.last)

emp1 = employee("corey", "schafer", 50000)
emp2 = employee("Test", "user", 60000)
emp1.first = "Correy"
emp1.var_inner = "old"
emp2.var_inner = "middle"

# print(emp1.fullname())
# print(emp2.fullname())
# print(emp1.var_inner," ",emp2.var_inner)
print(emp1.fullname())
print(employee.fullname(emp1))
print(emp1.fullname())
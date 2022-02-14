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
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(employee):
    def __init__(self, first, last, pay, Employees=None):
        super().__init__(first, last, pay)
        if Employees is None:
            self.Employees = []
        else:
            self.Employees = Employees
    
    def add_emp(self, emp):
        if emp not in self.Employees:
            self.Employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.Employees:
            self.Employees.remove(emp)
    
    def print_emps(self):
        for emp in self.Employees:
            print("-->",emp.fullname())
        
dev1 = Developer("Corey", "schafer", 50000, "Python")
dev2 = Developer("Test", "user", 60000, "Java")

mgr1 = Manager("Sue", "Smith", 90000, [dev1])

print(mgr1.email)

mgr1.add_emp(dev2)
mgr1.remove_emp(dev1)
mgr1.print_emps()

print(isinstance(mgr1,Manager))
print(issubclass(Manager,employee))






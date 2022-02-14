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

emp1 = employee("Corey", "schafer", 50000)
emp2 = employee("Test", "user", 60000)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
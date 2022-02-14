"""
This class enployee set the attribuites first and last name 
and was setted the attribuites email and full name to change 
set dinamic by the decorators @property, @name.setter and 
@name.deleter. With this class we can change dinamicly the 
attribuites that can be chanching whit others users.
"""

class employee:
    
    #Inizialing the attribuites first and last
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        
    #Email method to return the last email updated  
    @property
    def email(self) -> str:
    
        if type(self.first) == str and type(self.last) == str:
            return "{0:s}.{1:s}@gmail.com".format(self.first, self.last)
        else:
            raise TypeError("The first and last attribuite must be str format")
    
    #Fullname method to return the last fullname updated  
    @property
    def fullname(self) -> str:
        return "My full name is: {0:s} {1:s}".format(self.first, self.last)  
    
    #Fullname method to update the attribuites first and last
    @fullname.setter
    def fullname(self, name) -> None:
        first, last = name.split(" ")
        self.first = first
        self.last = last
    
    #Delete the first and last attribiutes and set in None
    @fullname.deleter
    def fullname(self):# -> str:
        print("Deleted Name!")
        self.first = None
        self.last = None

#Create a object from the employee class and print out
emp1 = employee("Jhon","Smith")
emp1.fullname = "Cristina Maria"
# emp1.first = "Jim"

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname
print(emp1.first)
# print(emp1.email)
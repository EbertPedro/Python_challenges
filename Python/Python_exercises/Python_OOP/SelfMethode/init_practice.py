class MyBehaviores:
    def __init__(self,name,address):
        self.name = name
        self.address = address
    
    def ReturnValues(self):
        return self.name, self.address
    
MyObject = MyBehaviores('Piter','Street Nro 13 Doly')
Name, Address = MyObject.ReturnValues()
print("Hello, my name is {0:s} and my address is {1:s}".format(Name,Address))



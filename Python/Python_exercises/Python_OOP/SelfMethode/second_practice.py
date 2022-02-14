#The object and self have the same ID
class check:
    def __init__(self):
        print("The address of self is: ",id(self))
    
obj = check()
# print(obj)
print("The object's address is: ",id(obj))
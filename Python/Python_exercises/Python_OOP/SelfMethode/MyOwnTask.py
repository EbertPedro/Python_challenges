print("Hello everubody let's twist again \n")

class Desk:
    def __init__(self, color_chair, color_desk, color_lamp, type_computer):
        self.color_chair = color_chair
        self.color_desk = color_desk
        self.color_lamp = color_lamp
        self.type_computer = type_computer
        print("I've inizialised the variables...")
    
    def Behaviores_desk(self):
        print("The process is starting................")
        print("The chair's color is {0:s}".format(self.color_chair))
        print("Loading.....................")
        print("The desk's color is {0:s}".format(self.color_desk))
        print("Loading.....................")
        print("The lamp's color is %s \n" %self.color_lamp)
        print("The process has ended")
        
MyOwnDesk = Desk("Brown","Light brown","White","Laptop")
MyOwnDesk.Behaviores_desk()
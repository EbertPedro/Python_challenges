"""
This class allowed us to add two classes in unit of lengths.
If the unit is not given, by default it is initialized in the 
unit of meter("m"). The result is given in the same unit of 
the first class given in the add. For example:
Length(5,"yd") + Length(15, "mm") the result is gigen in "yd"
input: Length(value,unit)
value --> int, float
unit  --> "mm", "cm", "m", "km", "in", "ft", "yd", "mi"
"""

class Length:
    __metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 } 
    
    def __init__(self, value, unit = "m" ):
        self.value = value
        self.unit = unit    
        
    def Converse2Metres(self):
        return self.value * Length.__metric[self.unit]   
    
    def __add__(self, other):
        l = self.Converse2Metres() + other.Converse2Metres()
        return Length(l / Length.__metric[self.unit], self.unit )    
    
    def __str__(self):
        return str(self.Converse2Metres()) 
    
    def __repr__(self):
        return 'Length({0:s}, "{1:s}")'.format(str(self.value),self.unit)
        # return "Length(" + str(self.value) + ", '" + self.unit + "')"
        
if __name__ == "__main__":
    med1 = Length(5,"yd") + Length(15, "mm") + Length(20, "cm")
    print("The __str__ method return: ", med1.__str__())   
    print("The __repr__ method return: ", med1.__repr__()) 
    recovery_med1 = eval(repr(med1))
    print(id(med1) == id(recovery_med1))

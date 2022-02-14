"""
This class allowed us to add two classes in unit of lengths.
If the unit of measurement is not given for either of the both terms, by default
it is initialized in the unit of meter("m") to the term of the unit not given. 
This programm we allow add the terms in three possicion, these are:
    Ex1: Length(5,"yd") + Length(12,"cm") --> Both objects are instances
                                              of the Length class
    Ex2: Length(5,"yd") + 4               --> The obj. is in the left side and the  
                                              term in the right side is an int or 
                                              float object.
    Ex3: med2 = Length(10, "cm")  
         med2 += 15                       --> We add with augmented arithmetic            
                                              assignments(+=,-=,*=,/=,etc), where
                                              the first is an object and the term 
                                              added is an int or float object.
         
    Ex4: med3 = 9 + Length(5, "yd")       --> The obj. is in the right side and the
                                              term in the left side is an int or
                                              float object.
The result is given in the same unit of the first class given in 
the add. For example:
Length(5,"yd") + Length(15, "mm") the result is given in "yd"
Length(12,"mm") + 4               the result is given in "mm"
4 + Length(12,"mm")               the result is given in "m"
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
        bool_self = isinstance(self,Length) 
        bool_other = isinstance(other,Length)
        
        if (bool_self==True) and (bool_other == True):
            l = self.Converse2Metres() + other.Converse2Metres()  
        elif (bool_self==True) and (bool_other == False):
            l = self.Converse2Metres() + other
        return Length(l / Length.__metric[self.unit], self.unit )   
    
    def __iadd__(self, other):
        bool_self = isinstance(self,Length) 
        bool_other = isinstance(other,Length)
        
        if (bool_self==True) and (bool_other == True):
            l = self.Converse2Metres() + other.Converse2Metres()  
        elif (bool_self==True) and (bool_other == False):
            l = self.Converse2Metres() + other
        
        self.value = l / Length.__metric[self.unit]
        return self        
  
    def __radd__(self, other):
        return Length.__add__(self,other)  
        
    def __str__(self):
        return str(self.Converse2Metres()) 
    
    def __repr__(self):
        return 'Length({0:s}, "{1:s}")'.format(str(self.value),self.unit)
        # return "Length(" + str(self.value) + ", '" + self.unit + "')"
        
if __name__ == "__main__":
    med1 = Length(5,"yd") + 4 + 5 
    print("The result is: {0:.3f} {1:s}".format(med1.value, med1.unit))  
     
    med2 = Length(10, "cm")
    med2 += 15
    print("The result is: {0:.3f} {1:s}".format(med2.value, med2.unit))      
     
    med3 = 9 + Length(5, "yd")
    print("The result is: {0:.3f} {1:s}".format(med3.value, med3.unit))
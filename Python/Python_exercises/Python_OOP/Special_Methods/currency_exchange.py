"""
This class allow us to add two specified classes of money, multiply the amout money
given by an scalar value as well as change currency money to another type desired.
To add money, if the unit of some of the money(i.e."USD","EUR",etc) is not given,
by default it is initialized with "USD" to the term of the money without unit.
Finally, if one of the terms of the add is of type int or float, this term is 
added assuming it has "USD" unit.  
This programm we allow add the terms in three possicion, these are:
    Ex1: Ccy(5,"USD") + Ccy(12,"CAD")   --> Both objects are instances
                                            of the Ccy class
    Ex2: Ccy(5,"CHF") + 4               --> The obj. is in the left side and the  
                                            term in the right side is an int or 
                                            float object(it has unit "USD" by default).
    Ex3: med2 = Ccy(10,"CAD")  
         med2 += 15                     --> We add with augmented arithmetic            
                                            assignments(+=,-=,*=,/=,etc), where
                                            the first is an object and the term 
                                            added can be an Ccy class, int or float.
    Ex4: med3 = 9 + Ccy(5, "EUR")       --> The obj. is in the right side and the
                                            term in the left side is an int or
                                            float object(it has unit "USD" by default).

The result is given in the same unit of the first class given in 
the add. For example:
Ccy(5,"EUR") + Ccy(15, "USD")   the result is given in "EUR"
Ccy(12,"CHF") + 4               the result is given in "CHF"
4 + Ccy(12,"JPY")               the result is given in "JPY"     
    
Also, this programm we allow multiply the terms in two possicion, these are:
    Ex1: 10 * Ccy(5,"USD")     --> The object of the class Ccy is in the right side 
                                   and the amount to multiply is in the left side,
                                   it can be int or float.
    Ex2: Ccy(5,"CHF") * 4      --> The object of the class Ccy is in the left side 
                                   and the amount to multiply is in the right side,
                                   it can be int or float.         
                                                                         
The result is given in the same unit of the class given in. For example:
Ccy(12,"CHF") * 4               the result is given in "CHF"
4 * Ccy(12,"JPY")               the result is given in "JPY" 

input: Ccy(value,unit)
value --> int, float
unit  --> "CHF", "CAD", "GBP", "JPY", "EUR", "USD"
"""

class Ccy:
    
    __rate_exchange = { 'CHF': 1.079905, 
                        'CAD': 0.78420723, 
                        'GBP': 1.3516275, 
                        'JPY': 0.0086734631, 
                        'EUR': 1.14266, 
                        'USD': 1 }
    
    def __init__(self,value,type_money="USD") -> None:
        self.value = value
        self.type_money = type_money
    
    def Change_to_dollar(self) -> float:
        money_in_dollar = self.value * Ccy.__rate_exchange[self.type_money]
        return money_in_dollar
    
    def Change_Ccy_unit(self,new_Ccy_unit) -> object:
        rate_old2new_money = Ccy.__rate_exchange[self.type_money]/Ccy.__rate_exchange[new_Ccy_unit]
        self.value = self.value * rate_old2new_money
        self.type_money = new_Ccy_unit
        return self
    
    def __add__(self,money_2) -> object:
    #It can add only in the next types: Ccy(20,"USD") + Ccy(33,"EUR") / Ccy(20,"USD") + 20
        if type(self).__name__ == "Ccy" and type(money_2).__name__ == "Ccy":
            amt_dollar = self.Change_to_dollar() + money_2.Change_to_dollar()
        elif type(self).__name__ == "Ccy" and (type(money_2) == int or type(money_2) == float):
            amt_dollar = self.Change_to_dollar() + money_2
        amt_type_money1 = amt_dollar * (1 / Ccy.__rate_exchange[self.type_money])
        type_money1 = self.type_money            
        return Ccy(amt_type_money1, type_money1)

    def __radd__(self,money_1) -> object:
        #It can add only in the next type: 20 + Ccy(33,"EUR")
        if type(self).__name__ == "Ccy" and (type(money_1) == int or type(money_1) == float):
            amt_type_money1 = self.Change_to_dollar() + money_1            
            type_money1 = "USD"            
            return Ccy(amt_type_money1, type_money1)
    
    def __iadd__(self,money_2) -> object:
        #It can add only in the next types: Ccy(20,"USD") + Ccy(33,"EUR") / Ccy(20,"USD") + 20
        if type(self).__name__ == "Ccy" and type(money_2).__name__ == "Ccy":
            amt_dollar = self.Change_to_dollar() + money_2.Change_to_dollar()
        elif type(self).__name__ == "Ccy" and (type(money_2) == int or type(money_2) == float):
            amt_dollar = self.Change_to_dollar() + money_2
        self.value = amt_dollar * (1 / Ccy.__rate_exchange[self.type_money])           
        return self
            
    def __mul__(self, amt2mul) -> object:
        if type(self).__name__ == "Ccy" and (type(amt2mul) == int or type(amt2mul) == float):
            self.value = self.value * amt2mul
            return Ccy(self.value, self.type_money)
        else:
            raise TypeError("Unsopported type for *: 'Ccy' and " + type(amt2mul).__name__)
    
    def __rmul__(self, amt2mul) -> object:
        return self.__mul__(amt2mul)
        
    def __str__(self) -> str:
        return "The sum of both money is: {0:.3f} {1:s}".format(self.value, self.type_money)
    
    def __repr__(self) -> str:
        return "Ccy({0:0.3f}, {1:s})".format(self.value, self.type_money)
    
my_add_money1 = 20 + Ccy(50,"CAD") + 10 * Ccy(33,"CHF") * 2 + 30
my_add_money1 += 20

print(my_add_money1.__str__())
print("Money exchanged to EUR: ",my_add_money1.Change_Ccy_unit("EUR"))

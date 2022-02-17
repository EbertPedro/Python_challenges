#Methode through List comprehension
"""
    Methode generalized with List comprenhension:
    list = [Expresion(x) for (values) in (collection or iterable)]
    
    Put into an templete of Foor loop:
    list = []
    for (values) in (collection or iterable):
        list.append(Expresion(values))
"""
squares = [x*x for x in range(10)]
print(squares)

squares2 = []
for x in range(10):
    squares2.append(x*x)
print(squares2)
print("Third....")

#List comprehension: Filtering applying if condition:
even_values = [x*x for x in range(10) if x == 2]
print(even_values)
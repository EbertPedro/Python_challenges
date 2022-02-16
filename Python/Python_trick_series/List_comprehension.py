#Methode through List comprehension
squares = [x*x for x in range(10)]
print(squares)

squares2 = []
for x in range(10):
    squares2.append(x*x)
print(squares2)
print("Third....")
"""
    Methode generalized with List comprenhension:
    list = [Expresion(x) for (values) in (collection or iterable)]
    
    Put into an templete of Foor loop:
    list = []
    for (values) in (collection or iterable):
        list.append(Expresion(values))
"""
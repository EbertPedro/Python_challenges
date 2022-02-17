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

""""
List comprehension: Filtering applying if condition:
Format: values = [expresion(x) for (value) in (collection or iterable) if (condition)]

Furthermore:
List comprehension with more than one line of code:
Format: values = [expression(x) 
                  for (value) in (collection or iterable) 
                  if (condition)]
"""
even_values = [x*x for x in range(10) if x == 2]
print("The first list filtered to even numbers is: {}".format(even_values))

#Rewriting the above example in more than one line of code
even_squares = [x * x
                for x in range(10)
                if x % 2 == 0]
print("The second list filtered to even numbers is: {}".format(even_values))
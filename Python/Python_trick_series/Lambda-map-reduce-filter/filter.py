"""
Apply same function to each element of an sequence
and return the element if it satisfy the condition of the function.
Take as imput: an Function f() and an iterable(set,tuples,list[m,n,p])
Output: New map object (f(m),f(n),f(p)) --> if each element satisfy the condition of f()
In implementation to get the values by: list(map(f(),[m,n,p]))
"""

# #We get the square of the list [4,3,2,1] by function and map
# numbers = [4,3,2,1]
# numbers2 = [6,7,10,2]
# def square(num):
#     return num%2 != 0

# map_square_iterator = filter(lambda x:x%2==0,numbers2)
# func_square_iterator = filter(square,numbers2)

# #We show an item one at time
# print(list(map_square_iterator))
# print(list(func_square_iterator)) 
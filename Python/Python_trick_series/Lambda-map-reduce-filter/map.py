"""
Apply same function to each element of an sequence
and return the modified list.
Take as imput: List [m,n,p] or an iterable and Function f()
Output: New list [f(m),f(n),f(p)]
In implementation: list(map(f(),[m,n,p]))
"""

#We get the square of the list [4,3,2,1] by function and map
lst = [4,3,2,1]
def square(lst):
    lst2 = []
    for num in lst:
        lst2.append(num*num)
    return lst2

map_square = list(map(lambda x:x*x,lst))
print(square(lst), map_square)

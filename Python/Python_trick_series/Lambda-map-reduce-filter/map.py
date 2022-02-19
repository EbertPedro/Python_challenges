"""
Apply same function to each element of an sequence
and return the modified list.
Take as imput: List [m,n,p] or an iterable and Function f()
Output: New map object (f(m),f(n),f(p))
In implementation to get the values: list(map(f(),[m,n,p]))
"""

#We get the square of the list [4,3,2,1] by function and map
lst = [4,3,2,1]
def square(lst):
    lst2 = []
    for num in lst:
        lst2.append(num*num)
    return lst2

map_square = map(lambda x:x*x,lst)
print(square(lst))

#We show an item one at time
print(next(map_square))
print(next(map_square))
print(next(map_square))
print(next(map_square))
# print(list(map_square)) 

"""
Apply same function to each element of an sequence
and return the modified list.
Take as imput: an iterable(set,tuples,list[m,n,p]) and Function f()
Output: New map object (f(m),f(n),f(p))
In implementation to get the values: list(map(f(),[m,n,p]))
"""

#We get the square of the list [4,3,2,1] by function and map
numbers = [4,3,2,1]
numbers2 = [6,7,10,2]
def square(num):
    return num*num

map_square_iterator = map(lambda x:x*x,numbers)
func_square_iterator = map(square,numbers)
map_sum_iterator = map(lambda x1,x2: x1+x2, numbers,numbers2)

#We show an item one at time
# print(next(func_square_iterator))
print(next(map_square_iterator)," ",next(func_square_iterator)," ",next(map_sum_iterator))
print(next(map_square_iterator)," ",next(func_square_iterator)," ",next(map_sum_iterator))
print(next(map_square_iterator)," ",next(func_square_iterator)," ",next(map_sum_iterator))
print(next(map_square_iterator)," ",next(func_square_iterator)," ",next(map_sum_iterator))
# print(list(map_square)) 

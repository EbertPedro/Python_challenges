"""
Generators: We are going to see the difference between
the return and yield operator in python. The key idea is 
the memory and the time taken to execute both generators.
"""

from traceback import print_tb


def square_numbers(nums):
    result = []
    for item in nums:
        result.append(item*item)
    return result

def square_numbers2(nums):
    for item in nums:
        yield (item*item)

#We see the result when print out the results
my_nums = square_numbers([1,2,3,4,5])
print(my_nums)
my_nums2 = square_numbers2([1,2,3,4,5])
print(my_nums2)

#The Yield object cannot show something because it only 
#show us when we print out by foor loop or an iterator
#we can print out one at a time by next or foor loop
# print(next(my_nums2))
# print(next(my_nums2))
# print(next(my_nums2))
# print(next(my_nums2))
# print(next(my_nums2))

for item in my_nums2:
    print(item, end=" ")
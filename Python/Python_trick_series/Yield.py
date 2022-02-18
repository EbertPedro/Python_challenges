#We are going to approach in the generator Yield 

from unittest import result


my_list = [x for x in range(1,10)]
print("My current list: ",my_list)

#Without generator
def process_list(my_list):
    result = [] #We are copy the values in an different address memory with the same name
    len_list = len(my_list) 
    for i in range(len_list):
        result.append(my_list[i] * 2)
    return result

#With generator
def process_list_generator(my_list):
    len_list = len(my_list)
    for i in range(len_list):
        yield i, my_list[i] * 2

for item in process_list(my_list):
    print(item, end=" ")

print(" ")
for index, item in process_list_generator(my_list):
    print(index, item)
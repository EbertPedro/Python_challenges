#We are going to approach in the generator Yield 

my_list = [x for x in range(1,10)]
print(my_list)

#Without generator
def process_list(my_list):
    len_list = len(my_list) 
    for i in range(len_list):
        my_list[i] *= 2
    return my_list[i]

#With generator
def process_list_generator(my_list):
    len_list = len(my_list)
    for i in range(len_list):
        return my_list[i] * 2
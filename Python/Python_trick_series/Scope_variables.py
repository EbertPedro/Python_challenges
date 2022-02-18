#We defiened the names of varaibles out of one function
#but this function also can call variables defined out of it

name = "carlos"
def my_func():
    full_name = name + " Abriera"
    print(full_name)

my_func()
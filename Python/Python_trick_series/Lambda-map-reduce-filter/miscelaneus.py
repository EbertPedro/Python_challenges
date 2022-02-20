#*************first*******************
# # list of vowels
# vowels = ['a', 'e', 'i', 'o', 'u']
# vowels_iter = iter(vowels)

# print(next(vowels_iter))    # 'a'
# print(next(vowels_iter))    # 'e'
# print(next(vowels_iter))    # 'i'
# print(next(vowels_iter))    # 'o'
# # print(next(vowels_iter))    # 'u'
# print(vowels_iter.__next__()) 

#***********second**********************
# class PrintNumber:
#     def __init__(self, max):
#         self.max = max

#     def __iter__(self):
#         self.num = 0
#         return self

#     def __next__(self):
#         if(self.num >= self.max):
#             raise StopIteration
#         self.num += 1
#         return self.num

# print_num = PrintNumber(3)

# # print_num_iter = iter(print_num)
# print_num_iter = print_num.__iter__()
# print(next(print_num_iter))  # 1
# print(next(print_num_iter))  # 2
# print(next(print_num_iter))  # 3

# # raises StopIteration
# # print(next(print_num_iter))

#*************third******************
# f = open("unbalanced_data.txt","w")
# f.write("This my first code with write function!!\n")
# f.write("This my first code with write function2!!\n")

#***************fouth*******************
# languages = ['Java', 'Python', 'JavaScript']
# versions = [14, 3, 6]

# result = zip(languages, versions)
# print(next(result))
# print(next(result))
# print(next(result))
# print(list(result))
# # Output: [('Java', 14), ('Python', 3), ('JavaScript', 6)]

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)
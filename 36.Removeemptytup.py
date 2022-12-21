# Remove empty tuples from a list

#1.
list = [1, 2, 3, (), 4, 5]
list.remove(()) 
print(list) # [1, 2, 3, 4, 5]


#2.
# def remove_empty(input_tuples):
#     input_tuples = [t for t in input_tuples if t]
#     return input_tuples
   
# input_tuples = [(), ('', ''), ('python', 'coding'), () , ('alpha', 'beta'), ('physics', 'maths'), ('', ''), ()]
# print(remove_empty(input_tuples)) # [('', ''), ('python', 'coding'), ('alpha', 'beta'), ('physics', 'maths'), ('', '')]
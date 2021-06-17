# Python program to find sum of elements in list
#1.method
# total = 0
# list1 = [11, 5, 17, 18, 23]

# for ele in range(0, len(list1)):
# 	total = total + list1[ele]

# print("Sum of all elements in given list: ", total)

#2.method using while loop

# total = 0
# ele = 0

# list1 = [11, 5, 17, 18, 23]

# while(ele < len(list1)):
# 	total = total + list1[ele]
# 	ele += 1
	
# print("Sum of all elements in given list: ", total)

# 3.elements in list using recursion

# list1 = [11, 5, 17, 18, 23]

# def sumOfList(list, size):
#     if (size == 0):
#         return 0
#     else:
#         return list[size - 1] + sumOfList(list, size - 1)

# total = sumOfList(list1, len(list1))

# print("Sum of all elements in given list: ", total)

# 4.using sum function

# list1 = [11, 5, 17, 18, 23]

# total = sum(list1)

# print("Sum of all elements in given list: ", total)

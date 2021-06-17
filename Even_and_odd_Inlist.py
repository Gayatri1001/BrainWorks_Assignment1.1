# Python program to print Even Numbers and odd numbers in a List
#1.
#for Even numbers
# list1 = [10, 21, 4, 45, 66, 93]
# for num in list1:
# 	if num % 2 == 0:
#          print(num, end = " ")

#for Odd numbers
# list1 = [10, 21, 4, 45, 66, 93]
# for num in list1:
# 	if num % 2 != 0:
#          print(num, end = " ")

#2.using while loop
#for Even numbers
# list1 = [10, 21, 4, 45, 66, 93]
# num = 0	
# while(num < len(list1)):
# 	if num % 2 == 0:
#          print(list1[num], end = " ")
	
# 	num += 1
	
#for Odd numbers
# list1 = [10, 21, 4, 45, 66, 93]
# num = 0

# while(num < len(list1)):
	
# 	if num % 2 != 0:
# 	 print(list1[num], end = " ")
	
# 	num += 1
	
#3.using list comprehension
#for Even numbers
# list1 = [10, 21, 4, 45, 66, 93]

# even_nos = [num for num in list1 if num % 2 == 0]

# print("Even numbers in the list: ", even_nos)

#for Odd numbers
# list1 = [10, 21, 4, 45, 66, 93]

# odd_nos = [num for num in list1 if num % 2 != 0]

# print("odd numbers in the list: ", odd_nos)


# 4.using lambda function
# # for Even numbers
# list1 = [10, 21, 4, 45, 66, 93, 11]

# even_nos = list(filter(lambda x: (x % 2 == 0), list1))

# print("Even numbers in the list: ", even_nos)

# for Odd numbers
# list1 = [10, 21, 4, 45, 66, 93, 11]

# odd_nos = list(filter(lambda x: (x % 2 != 0), list1))

# print("odd numbers in the list: ", odd_nos)


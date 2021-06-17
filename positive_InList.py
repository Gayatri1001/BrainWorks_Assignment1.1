# Python program to print positive Numbers in a List
#1.
# list1 = [11, -21, 0, 45, 66, -93]

# for num in list1:
	
# 	if num > 0:
# 	 print(num, end = " ")

#2.using while loop
# list1 = [-10, 21, -4, -45, -66, 93]
# num = 0
	
# while(num < len(list1)):
	
# 	if list1[num] > 0:
# 		print(list1[num], end = " ")
	
# 	num += 1
	
#3.using list comprehension

# list1 = [-10, -21, -4, 45, -66, 93]

# pos_nos = [num for num in list1 if num > 0]

# print("Positive numbers in the list: ", *pos_nos)

# #4.using lamda expression
# list1 = [-10, 21, 4, -45, -66, 93, -11]

# pos_nos = list(filter(lambda x: (x > 0), list1))

# print("Positive numbers in the list: ", *pos_nos)


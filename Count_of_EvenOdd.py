# Python program to count Even and Odd numbers in a List
#1.using for loop
# list1 = [10, 21, 4, 45, 66, 93, 1]

# even_count, odd_count = 0, 0

# for num in list1:
# 	if num % 2 == 0:
# 		even_count += 1

# 	else:
# 		odd_count += 1
		
# print("Even numbers in the list: ", even_count)
# print("Odd numbers in the list: ", odd_count)

#2.using while loop
# list1 = [10, 21, 4, 45, 66, 93, 11]

# even_count, odd_count = 0, 0
# num = 0
	
# while(num < len(list1)):
	
# 	if list1[num] % 2 == 0:
# 		even_count += 1
# 	else:
# 		odd_count += 1
	
# 	num += 1
	
# print("Even numbers in the list: ", even_count)
# print("Odd numbers in the list: ", odd_count)

#3.using lambda expression
# list1 = [10, 21, 4, 45, 66, 93, 11]

# odd_count = len(list(filter(lambda x: (x%2 != 0) , list1)))
# even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))

# print("Even numbers in the list: ", even_count)
# print("Odd numbers in the list: ", odd_count)

#4.using list comprehension

# list1 = [10, 21, 4, 45, 66, 93, 11]

# only_odd = [num for num in list1 if num % 2 == 1]
# odd_count = len(only_odd)

# print("Even numbers in the list: ", len(list1) - odd_count)
# print("Odd numbers in the list: ", odd_count)

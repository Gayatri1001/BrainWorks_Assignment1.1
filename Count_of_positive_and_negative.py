# Python program to count positive and negative numbers in a List
#1.method using for loop
list1 = [10, -21, 4, -45, 66, -93, 1]

pos_count, neg_count = 0, 0

for num in list1:
	
	if num >= 0:
		pos_count += 1

	else:
		neg_count += 1
		
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)

#2.using while loop
list1 = [-10, -21, -4, -45, -66, 93, 11]

pos_count, neg_count = 0, 0
num = 0
	
while(num < len(list1)):
	
	if list1[num] >= 0:
		pos_count += 1
	else:
		neg_count += 1
	
	num += 1
	
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)

#3.using lambda expression

list1 = [10, -21, -4, 45, 66, 93, -11]

neg_count = len(list(filter(lambda x: (x < 0), list1)))

pos_count = len(list(filter(lambda x: (x >= 0), list1)))

print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)

#4.using list comprehension
list1 = [-10, -21, -4, -45, -66, -93, 11]

only_pos = [num for num in list1 if num >= 1]
pos_count = len(only_pos)

print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", len(list1) - pos_count)

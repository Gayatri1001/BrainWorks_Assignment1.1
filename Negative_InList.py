# Python program to print negative Numbers in a List
#1.
list1 = [11, -21, 0, 45, 66, -93]

for num in list1:
	
	if num < 0:
	 print(num, end = " ")

#2.using while loop
list1 = [-10, 21, -4, -45, -66, 93]
num = 0
	
while(num < len(list1)):
	
	if list1[num] < 0:
		print(list1[num], end = " ")
	
	num += 1
	
#3.using list comprehension

list1 = [-10, -21, -4, 45, -66, 93]

neg_nos = [num for num in list1 if num < 0]

print("Negative numbers in the list: ", *neg_nos)

#4.using lamda expression
list1 = [-10, 21, 4, -45, -66, 93, -11]

neg_nos = list(filter(lambda x: (x < 0), list1))

print("Negative numbers in the list: ", *neg_nos)


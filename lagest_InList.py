# Python program to find largest number in a list
#1.using sort method
list1 = [10, 20, 4, 45, 99]

list1.sort()

print("Largest element is:", list1[-1])

#2 using max function

list1 = [10, 20, 4, 45, 99]

print("Largest element is:", max(list1))

#3.

def myMax(list1):

	max = list1[0]

	for x in list1:
		if x > max :
			max = x
	
	return max

list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))

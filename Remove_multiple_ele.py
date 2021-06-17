# Python program to remove multiple elements from a list
#1.method
list1 = [11, 5, 17, 18, 23, 50]

for ele in list1:
	if ele % 2 == 0:
		list1.remove(ele)

print("New list after removing all even numbers: ", list1)

#2 method using list comprehension

list1 = [11, 5, 17, 18, 23, 50]

list1 = [ elem for elem in list1 if elem % 2 != 0]

print(*list1)

#3. using slicing

list1 = [11, 5, 17, 18, 23, 50]

del list1[1:5]

print(*list1)

#4.method
list1 = [11, 5, 17, 18, 23, 50]

unwanted_num = {11, 5}

list1 = [ele for ele in list1 if ele not in unwanted_num]

print("New list after removing unwanted numbers: ", list1)

#5.
list1 = [11, 5, 17, 18, 23, 50]

unwanted = [0, 3, 4]

for ele in sorted(unwanted, reverse = True):
    
	del list1[ele]

print (*list1)


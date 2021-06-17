#1.Python program to copy or clone a list
# Using the Slice Operator

# def clone(list1):
#     return list1[:]
    
# l1=[10,20,30,40,50]
# print(f"original list{l1}")
# output=clone(l1)
# print(f"copy of l1 list{output}")

# 2.Using the in-built function extend()

# def cloning(list1):
#     copy_list=[]
#     copy_list.extend(list1)
#     return copy_list

# l1=[10,20,30,40,50]
# print(f"original list{l1}")
# output=cloning(l1)
# print(f"After cloning{output}")

# 3.Using the in-built function list()
# def Cloning(list1):
# 	list_copy = list(list1)
# 	return list_copy

# l1 = [4, 8, 2, 10, 15, 18]
# output = Cloning(l1)
# print("Original List:", l1)
# print("After Cloning:", output)

# 4.Using list comprehension
# def Cloning(list1):
# 	li_copy = [i for i in list1]
# 	return li_copy

# l1 = [4, 8, 2, 10, 15, 18]
# output = Cloning(l1)
# print("Original List:", l1)
# print("After Cloning:", output)

# 5.Using append()

# def Cloning(li1):
# 	li_copy =[]
# 	for item in li1: li_copy.append(item)
# 	return li_copy

# li1 = [4, 8, 2, 10, 15, 18]
# li2 = Cloning(li1)
# print("Original List:", li1)
# print("After Cloning:", li2)

# 6.Using bilt-in method copy()
# def Cloning(li1):
# 	li_copy =[]
# 	li_copy = li1.copy()
# 	return li_copy

# li1 = [4, 8, 2, 10, 15, 18]
# li2 = Cloning(li1)
# print("Original List:", li1)
# print("After Cloning:", li2)

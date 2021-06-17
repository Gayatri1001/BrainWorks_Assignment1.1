# Python program to sort one list using the other list
#.1 using zip method
def sort_list(list1, list2):

	zipped_pairs = zip(list2, list1)

	z = [x for _, x in sorted(zipped_pairs)]
	
	return z
	
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))

x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
y = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))

#2.By using Dictionary, list comprehension, lambda function

def sorting_of_element(list1,list2):

	f_1 = {}
	
	final_list = []
	
	f_1 = {list1[i]: list2[i] for i in range(len(list2))}
	
	f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}
	
	for i in f_lst.keys():
		final_list.append(i)
	return final_list
		
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]


sorting_of_element(list1,list2)

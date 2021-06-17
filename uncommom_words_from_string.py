# # Python3 program to find a list of uncommon words
# #1.Function to return all uncommon words
# def UncommonWords(A, B):

# 	count = {}
	
# 	for word in A.split():
# 		count[word] = count.get(word, 0) + 1

# 	for word in B.split():
# 		count[word] = count.get(word, 0) + 1

# 	return [word for word in count if count[word] == 1]

# A = "Geeks for Geeks"
# B = "Learning from Geeks for Geeks"

# print(UncommonWords(A, B))

# #2.
# def uncommon(a,b):
# 	list_a = a.split()
# 	list_b = b.split()
# 	uc = ''
# 	for i in list_a:
# 		if i not in list_b:
# 			uc = uc+" "+i
# 	for j in list_b:
# 		if j not in list_a:
# 			uc = uc+" "+j

# 	return uc

# a = "apple banana mango"
# b = "banana fruits mango"
# print(uncommon(a,b))

# #3.using built in function symmetric_difference

def uncommon(a,b):
  a=a.split()
  b=b.split()
  k=set(a).symmetric_difference(set(b))
  return k

if __name__=="__main__":
  a="apple banana mango"
  b="banana fruits mango"
print(list(uncommon(a,b)))

#4.method
def uncommon(A, B):
	un_comm = [i for i in "".join(B).split() if i not in "".join(A).split()]
	return un_comm

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
print(uncommon(A, B))

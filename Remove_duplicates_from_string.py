#Python | Remove all duplicates words from a given sentence

#1.using external library
from collections import Counter

def remov_duplicates(input):

	input = input.split(" ")

	for i in range(0, len(input)):
		input[i] = "".join(input[i])

	UniqW = Counter(input)

	s = " ".join(UniqW.keys())
	print (s)

if __name__ == "__main__":
	input = 'Python is great and Java is also great'
	remov_duplicates(input)


# 2.Program without using any external library
s = "Python is great and Java is also great"
l = s.split()
k = []
for i in l:

	if (s.count(i)>1 and (i not in k)or s.count(i)==1):
		k.append(i)
print(' '.join(k))

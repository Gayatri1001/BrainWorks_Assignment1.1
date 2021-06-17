# Python code to demonstrate method to remove i'th character 
# 1.Naive Method

test_str = "GeeksForGeeks"

print ("The original string is : " + test_str)

new_str = ""

for i in range(len(test_str)):
	if i != 2:
		new_str = new_str + test_str[i]

print ("The string after removal of i'th character : " + new_str)

#2.using str.replace

test_str = "GeeksForGeeks"

print ("The original string is : " + test_str)

new_str = test_str.replace('e', '')

print ("The string after removal of i'th character( doesn't work) : " + new_str)

new_str = test_str.replace('s', '', 1)

print ("The string after removal of i'th character(works) : " + new_str)

#3.using slice with concatination

test_str = "GeeksForGeeks"

print ("The original string is : " + test_str)

new_str = test_str[:2] + test_str[3:]

print ("The string after removal of i'th character : " + new_str)

#4.using str.join and list comprehension

test_str = "GeeksForGeeks"

print ("The original string is : " + test_str)

new_str = ''.join([test_str[i] for i in range(len(test_str)) if i != 2])

print ("The string after removal of i'th character : " + new_str)

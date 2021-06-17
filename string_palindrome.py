#1.using slicing

str1=input("Enter some string:")

if str1==str1[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")

#2.using function

def isPalindrome(s):
	return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")

#3.using revered function and join method

def isPalindrome(s):
	
	rev = ''.join(reversed(s))

	if (s == rev):
		return True
	return False

s = "malayalam"
ans = isPalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")

#4.using one extra variable

x = "malayalam"

w = ""
for i in x:
	w = i + w

if (x == w):
	print("Yes")
else:
	print("No")



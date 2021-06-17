# . Python | Check if a Substring is Present in a Given String Find length of a string 
# 1.
#---------------------------------
def check(string, sub_str):
	if (string.find(sub_str) == -1):
		print("NO")
	else:
		print("YES")
		  
string = "python is best langauge"
sub_str ="pooja"
check(string, sub_str)

#2.
#-----------------------------------
# string="python is best langauge"
# text=input("Enter some string:\n")

# if text in string:
# 	spam=True
# else:
# 	spam=False

# if(spam):
# 	print("this text is spam")
# else:
# 	print("this text is not spam")

#3.
#--------------------------------------
# import re

# MyString1 = "A geek in need is a geek indeed"
# MyString2 ="geek"

# if re.search( MyString2, MyString1 ):
# 	print("YES,string '{0}' is present in string '{1}' " .format(MyString2,MyString1))
# else:
# 	print("NO,string '{0}' is not present in string {1} " .format(MyString2, MyString1) )


#4.
#----------------------------------------
# def check(s2, s1):
# 	if (s2.count(s1)>0):	
# 		print("YES")
# 	else:
# 		print("NO")
			
# s2 = "A geek in need is a geek indeed"
# s1 ="geek"
# check(s2, s1)

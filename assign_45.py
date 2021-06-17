# Python code to count number of matching
# characters in a pair of strings
#1.method
def count(str1, str2):
	c, j = 0, 0
	
	for i in str1:	
		
		if str2.find(i)>= 0 and j == str1.find(i):
			c += 1
		j += 1
	print ('No. of matching characters are : ', c)

def main():
	str1 ='aabcddekll12@'
	str2 ='bb2211@55k'
	count(str1, str2) 

if __name__=="__main__":
	main()

#2.method
def count(str1 ,str2) :
	
	set_string1 = set(str1)

	set_string2 = set(str2)

	matched_characters = set_string1 & set_string2

	print("No. of matching characters are : " + str(len(matched_characters)) )


if __name__ == "__main__" :

	str1 = 'aabcddekll12@' 
	str2 = 'bb2211@55k'	 

	count( str1 , str2 )
	
#3.method
import re
ip1 = "geeks"
ip2 = "geeksonly"

c = 0
for i in ip1:
	if re.search(i,ip2):
		c=c+1
print("No. of matching characters are ", c)


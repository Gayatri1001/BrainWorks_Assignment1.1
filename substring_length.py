# Check if a Substring is Present in a Given String Find length of a string in python
# 1. Using user defined function.
# def check(string, sub_str):
#     if (string.find(sub_str) == -1):
#         print("NO")
#     else:
#         print("YES")
            
# string = "geeks for geeks"
# sub_str ="geek"
# check(string, sub_str)
# ##OUTPUT##
# # YES

# # 2. Using “count()” method:-
# def check(s2, s1): 
#     if (s2.count(s1)>0):     
#         print("YES") 
#     else: 
#         print("NO") 
              
# s2 = "A geek in need is a geek indeed"
# s1 ="geek"
# check(s2, s1) 
# # ##OUTPUT##
# # # YES

#3. 3: Using regular expressions:-
# When you have imported the re module, you can start using regular expressions.
# import re
  
# # Take input from users
# MyString1 =  "A geek in need is a geek indeed"
# MyString2 ="geek"
  
# # re.search() returns a Match object if there is a match anywhere in the string
# if re.search( MyString2, MyString1 ):
#     print("YES,string '{0}' is present in string '{1}' " .format(MyString2,MyString1))
# else:
#     print("NO,string '{0}' is not present in string {1} " .format(MyString2, MyString1) )
# ##OUTPUT##
# # YES,string 'geek' is present in string 'A geek in need is a geek indeed' 



# # Check for URL in a String Execute a String of Code in
# # 1.
# import re
  
# def Find(string):
  
#     # findall() has been used 
#     # with valid conditions for urls in string
#     regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
#     url = re.findall(regex,string)      
#     return [x[0] for x in url]
      
# # Driver Code
# string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org/'
# print("Urls: ", Find(string))

# 2.
# import re
# text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
# urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
# print("Original string: ",text)
# print("Urls: ",urls)

# 3.
# Program to find the URL from an input string
# import re
# def url(str):
#    # findall() has been used
#    # with valid conditions for urls in string
#    ur = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
#    return ur
#    # Driver Code
#    str = 'https://auth.mywebsite.org / user / python program / http://www.mywebsite.org/'
# print("Url is :: ", url(str))
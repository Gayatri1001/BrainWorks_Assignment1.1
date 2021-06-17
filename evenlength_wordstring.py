# Python program to print even length words in a string
# 1. 
def printWords(s):
      
    # split the string 
    s = s.split(' ') 
      
    # iterate in words of string 
    for word in s: 
          
        # if length is even 
        if len(word)%2==0:
            print(word) 
  
  
# Driver Code 
s = "i am muskan" 
printWords(s) 

## OUTPUT ##
# am
# muskan
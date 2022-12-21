# Find all close matches of input string from a list
# 1.
# from difflib import get_close_matches 
  
# def closeMatches(patterns, word): 
#      print(get_close_matches(word, patterns)) 
  
# if __name__ == "__main__": 
#     word = 'appel'
#     patterns = ['ape', 'apple', 'peach', 'puppy'] 
#     closeMatches(patterns, word) # ['apple', 'ape']


# #2.
# import difflib
# list_of_words = ['ape', 'apple', 'peach', 'puppy']
# x = difflib.get_close_matches("appel", list_of_words)
# print(x) # ['apple', 'ape']

# a =(1,2,3,4,5)
# sum1=sum(a)
# print(sum1)

s=[10,20,0,5,0,30]
for x in range(len(s)):
    s.pop()
print(s)


    
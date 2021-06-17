# # Find all close matches of input string from a list
# # 1.
# from difflib import get_close_matches
  
# def closeMatches(patterns, word):
#      print(get_close_matches(word, patterns))
  
# # Driver program
# if __name__ == "__main__":
#     word = 'appel'
#     patterns = ['ape', 'apple', 'peach', 'puppy']
#     closeMatches(patterns, word)

# # 2.
# ## initializing the string list
# strings = ["Lion", "Li", "Tiger", "Tig"]
# element = "Lion"
# for string in strings:
#    ## checking for the condition mentioned above
#    if string.startswith(element) or element.startswith(string):
#       ## printing the eligible string
#       print(string, end = " ")
# print()
# # Find all duplicate characters in string
# # 1.
# ## initializing string
# string = "tutorialspoint"
# ## initializing a list to append all the duplicate characters
# duplicates = []
# for char in string:
#    ## checking whether the character have a duplicate or not
#    ## str.count(char) returns the frequency of a char in the str
#    if string.count(char) > 1:
#    ## appending to the list if it's already not present
#    if char not in duplicates:
#    duplicates.append(char)
# print(*duplicates)

# 2.
# ## initializing string
# string = "tutorialspoint"
# ## initializing a dictionary
# duplicates = {}
# for char in string:
#    ## checking whether the char is already present in dictionary or not
#    if char in duplicates:
#       ## increasing count if present
#       duplicates[char] += 1
#    else:
#       ## initializing count to 1 if not present
#       duplicates[char] = 1
# for key, value in duplicates.items():
#    if value > 1:
#       print(key, end = " ")
# print()

# 3.
# from collections import Counter
  
# def find_dup_char(input):
  
#     # now create dictionary using counter method
#     # which will have strings as key and their 
#     # frequencies as value
#     WC = Counter(input)
#     j = -1
      
      
#     # Finding no. of  occurrence of a character
#     # and get the index of it.
#     for i in WC.values():
#         j = j + 1
#         if( i > 1 ):
#             print WC.keys()[j],
  
# # Driver program
# if __name__ == "__main__":
#     input = 'geeksforgeeks'
#     find_dup_char(input)

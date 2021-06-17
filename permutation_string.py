# # Permutation of a given string using inbuilt function
# # 1.
# ## importing the module
# import itertools
# ## initializing a string
# string = "XYZ"
# ## itertools.permutations method
# permutaion_list = list(itertools.permutations(string))
# ## printing the obj in list
# print("-----------Permutations Of String In Tuples----------------")
# print(permutaion_list)
# ## converting the tuples to string using 'join' method
# print("-------------Permutations In String Format-----------------")
# for tup in permutaion_list:
#    print("".join(tup))

# 2.
# from itertools import permutations
  
# def allPermutations(str):
       
#      # Get all permutations of string 'ABC'
#      permList = permutations(str)
  
#      # print all permutations
#      for perm in list(permList):
#          print (''.join(perm))
        
# # Driver program
# if __name__ == "__main__":
#     str = 'ABC'
#     allPermutations(str)

# 3.
# from itertools import permutations
# import string
  
# s = "GEEK"
# a = string.ascii_letters
# p = permutations(s)
  
# # Create a dictionary
# d = []
# for i in list(p):
  
#     # Print only if not in dictionary
#     if (i not in d):
#         d.append(i)
#         print(''.join(i))

# 4.
# def toString(List):
#     return ''.join(List)
  
# # Function to print permutations of string
# # This function takes three parameters:
# # 1. String
# # 2. Starting index of the string
# # 3. Ending index of the string.
# def permute(a, l, r):
#     if l == r:
#         print toString(a)
#     else:
#         for i in xrange(l, r + 1):
#             a[l], a[i] = a[i], a[l]
#             permute(a, l + 1, r)
#             a[l], a[i] = a[i], a[l] # backtrack
  
# # Driver program to test the above function
# string = "ABC"
# n = len(string)
# a = list(string)
# permute(a, 0, n-1)

# 5.
# from itertools import permutations
# print [''.join(p) for p in permutations('ABC')]

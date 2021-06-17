# # String slicing in Python to check if a string can become empty by recursive deletion
# # 1.
# # # def checkEmpty(input, pattern): 
        
# #     # If both are empty  
# #     if len(input)== 0 and len(pattern)== 0: 
# #          return 'true'
    
# #     # If only pattern is empty 
# #     if len(pattern)== 0: 
# #          return 'true'
    
# #     while (len(input) != 0): 
  
# #         # find sub-string in main string 
# #         index = input.find(pattern) 
  
# #         # check if sub-string founded or not 
# #         if (index ==(-1)): 
# #           return 'false'
  
# #         # slice input string in two parts and concatenate 
# #         input = input[0:index] + input[index + len(pattern):]              
  
# #     return 'true'
    
# # # Driver program 
# # if __name__ == "__main__": 
# #     input ='GEEGEEKSKS'
# #     pattern ='GEEKS'
# #     print (checkEmpty(input, pattern))

# # 2.
# # Returns true if str can be made empty by
# # recursively removing sub_str.
# # def canBecomeEmpty(string, sub_str):
# #     while len(string) > 0:
 
# #         # idx: to store starting index of sub-
# #         #     string found in the original string
# #         idx = string.find(sub_str)
 
# #         if idx == -1:
# #             break
 
# #         # Erasing the found sub-string from
# #         # the original string
# #         string = string.replace(sub_str, "", 1)
 
# #     return (len(string) == 0)
 
# # # Driver code
# # if __name__ == "__main__":
# #     string = "GEEGEEKSKS"
# #     sub_str = "GEEKS"
# #     if canBecomeEmpty(string, sub_str):
# #         print("Yes")
# #     else:
# #         print("No")

# # 3.
# def is_valid(string, sub_string):
#        # checking the lengths of string and sub_string
#    if len(string) > 0 and len(sub_string):
#       # iterating until string becomes empty
#       while len(string) > 0:
#          # finding the sub_string in string
#          index = string.find(sub_string)
#       # checking whether its present or not
#       if index == -1:
#          # returning false
#    return False
#    # removind the sub_string
#    string = string[0: index] + string[index + len(sub_string):]
#    # returning True
#    return True
#    else:
#       # returning False
#    return False
#    if __name__ == '__main__':
#       # initializing the string and string
#       string = 'tutorialstutorialspointpoint'
#       sub_string = 'tutorialspoint'
# # invoking the method
# print(is_valid(string, sub_string))
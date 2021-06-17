# # String slicing in Python to rotate a string
# # 1.
# def rotate(input,d): 
  
#     # slice string in two parts for left and right 
#     Lfirst = input[0 : d] 
#     Lsecond = input[d :] 
#     Rfirst = input[0 : len(input)-d] 
#     Rsecond = input[len(input)-d : ] 
  
#     # now concatenate two parts together 
#     print ("Left Rotation : ", (Lsecond + Lfirst) )
#     print ("Right Rotation : ", (Rsecond + Rfirst)) 
  
# # Driver program 
# if __name__ == "__main__": 
#     input = 'GeeksforGeeks'
#     d=2
#     rotate(input,d) 

# 2.
# In-place rotates s towards left by d
# def leftrotate(s, d):
#     tmp = s[d : ] + s[0 : d]
#     return tmp
   
# # In-place rotates s
# # towards right by d
# def rightrotate(s, d):
   
#    return leftrotate(s, len(s) - d)
 
# # Driver code
# if __name__=="__main__":
     
#     str1 = "GeeksforGeeks"
#     print(leftrotate(str1, 2))
  
#     str2 = "GeeksforGeeks"
#     print(rightrotate(str2, 2))
 
# # 3.
# def rotate(input,d):
#        # Slice string in two parts for left and right
#    Lfirst = input[0 : d]
#    Lsecond = input[d :]
#    Rfirst = input[0 : len(input)-d]
#    Rsecond = input[len(input)-d : ]
#    print ("Left Rotation : ", (Lsecond + Lfirst) )
#    print ("Right Rotation : ", (Rsecond + Rfirst) )
#       # Driver program
#    if __name__ == "__main__":
#       str = input("Enter String ::>")
# d=2
# rotate(str,d)

# 4.
# python code to show string slicing
# x = "India is my nation"
# # printing substring starting from 2nd index to 13th index with a gap of 2 characters
# print(x[2:13:2])
# #printing substring from 12th index to the last
# print(x[12:])
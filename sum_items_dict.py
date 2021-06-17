# # # # # Python program to find the sum of all items in a dictionary
# # # # # 1.
# # # # # Python3 Program to find sum of 
# # # # # all items in a Dictionary
  
# # # # # Function to print sum
# # # # def returnSum(myDict):
      
# # # #     sum = 0
# # # #     for i in myDict:
# # # #         sum = sum + myDict[i]
      
# # # #     return sum
  
# # # # # Driver Function
# # # # dict = {'a': 100, 'b':200, 'c':300}
# # # # print("Sum :", returnSum(dict))

# # # # 2. # Python3 Program to find sum of 
# # # # all items in a Dictionary
  
# # # # Function to print sum
# # # def returnSum(dict):
      
# # #      sum = 0
# # #      for i in dict.values():
# # #            sum = sum + i
       
# # #      return sum
  
# # # # Driver Function
# # # dict = {'a': 100, 'b':200, 'c':300}
# # # print("Sum :", returnSum(dict))

# # # 3.
  
# # # # Function to print sum
# # # def returnSum(dict):
      
# # #      sum = 0
# # #      for i in myDict:
# # #            sum = sum + dict[i]
       
# # #      return sum
  
# # # # Driver Function
# # # dict = {'a': 100, 'b':200, 'c':300}
# # # print("Sum :", returnSum(dict))

# # # 4.
# # my_dict = {'data1':100,'data2':-54,'data3':247}
# # print(sum(my_dict.values()))

# # 5.
# # myDict = {'x': 250, 'y':500, 'z':410}
# # print("Dictionary: ", myDict)
# # total = 0

# # # Print Values using get
# # for i in myDict:
# #     total = total + myDict[i]
    
# # print("\nThe Total Sum of Values : ", total)

# # 6.
# # sum function
# def Sum(myDict):
#    sum_ = 0
#    for i in myDict:
#       sum_ = sum_ + myDict[i]
#    return sum_
# # Driver Function
# dict = {'T': 1, 'U':2, 'T':3, 'O':4, 'R':5}
# print("Sum of dictionary values :", Sum(dict))
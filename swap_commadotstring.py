# # Swap commas and dots in a String
# # 1.
# def Replace(str1):
#     maketrans = str1.maketrans
#     final = str1.translate(maketrans(',.', '.,', ' '))
#     return final.replace(',', ", ")
 
 
# # Driving Code
# string = "14, 625, 498.002"
# print(Replace(string))

# # 2.
# def Replace(str1):
#     str1 = str1.replace(', ', 'third')
#     str1 = str1.replace('.', ', ')
#     str1 = str1.replace('third', '.')
#     return str1
     
# string = "14, 625, 498.002"
# print(Replace(string))


# # 3.
# amount = "32.054,23"
# maketrans = amount.maketrans
# amount = amount.translate(maketrans(',.', '.,'))
# print(amount)

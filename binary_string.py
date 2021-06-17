# # Check if a given string is binary string or not
# # 1. Using Set:-
# # function for checking the
# # string is accepted or not
# def check(string):

#     # set function convert string
#     # into set of characters .
#     p = set(string)

#     # declare set of '0', '1' .
#     s = {'0', '1'}

#     # check set p is same as set s
#     # or set p contains only '0'
#     # or set p contains only '1'
#     # or not, if any one condition
#     # is true then string is accepted
#     # otherwise not .
#     if s == p or p == {'0'} or p == {'1'}:
#         print("Yes")
#     else:
#         print("No")


# # driver code
# if __name__ == "__main__":

#     string = "101010000111"

#     # function calling
#     check(string)


# # 2. Simple Iteration
# # function for checking the
# # string is accepted or not
# def check2(string):

#     # initialize the variable t
#     # with '01' string
#     t = '01'

#     # initialize the variable count
#     # with 0 value
#     count = 0

#     # looping through each character
#     # of the string .
#     for char in string:

#         # check the character is present in
#         # string t or not.
#         # if this condition is true
#         # assign 1 to the count variable
#         # and break out of the for loop
#         # otherwise pass
#         if char not in t:
#             count = 1
#             break
#         else:
#             pass

#     # after coming out of the loop
#     # check value of count is non-zero or not
#     # if the value is non-zero the en condition is true
#     # and string is not accepted
#     # otherwise string is accepted
#     if count:
#         print("No")
#     else:
#         print("Yes")


# # driver code
# if __name__ == "__main__":

#     string = "001021010001010"

#     # function calling
#     check2(string)


# # 3.
# stringA = '0110101010111'
# b = {'0', '1'}
# t = set(stringA)

# if b == t or t == {'0'} or t == {'1'}:
#     print("StringA is a binary string.")
# else:
#     print("StringA is not a binary string.")

# stringB = '0120101010111'
# u = set(stringB)

# if b == u or u == {'0'} or u == {'1'}:
#     print("StringB is a binary string.")
# else:
#     print("StringB is not a binary string.")

# # 4. 
# def ck_binary(x):
#     # Converting input value into set
#     ip_set = set(x)
# # Declaring new set with values 0 and 1
#     bin_set = { '0', '1'}
# # Check if input string elements is 0 , 1
#     if bin_set == ip_set or ip_set == {'0'} or ip_set == {'1'}:
#         print("The string {0} is binary string!".format(x))
#     else:
#         print("The string {0} is not a binary string!".format(x))
# ip_str = input("Enter the string to check whether it's a binary string : ")
# ck_binary(ip_str)
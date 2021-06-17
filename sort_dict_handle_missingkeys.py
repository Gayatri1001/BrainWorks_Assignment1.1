# # # # Sort Python Dictionaries by Key or Value Handling missing keys in dict.
# # # # 1.
# # # country_code = {'India' : '0091',
# # #                 'Australia' : '0025',
# # #                 'Nepal' : '00977'}
  
# # # # search dictionary for country code of India
# # # print(country_code.get('India', 'Not Found'))
  
# # # # search dictionary for country code of Japan
# # # print(country_dict.get('Japan', 'Not Found'))

# # # 2.
# # # country_code = {'India' : '0091',
# # #                 'Australia' : '0025',
# # #                 'Nepal' : '00977'}
  
# # # # Set a default value for Japan
# # # country_code.setdefault('Japan', 'Not Present') 
  
# # # # search dictionary for country code of India
# # # print(country_code['India'])
  
# # # # search dictionary for country code of Japan
# # # print(country_code['Japan'])


# # # 3.

# # # importing "collections" for defaultdict
# # import collections
  
# # # declaring defaultdict
# # # sets default value 'Key Not found' to absent keys
# # defd = collections.defaultdict(lambda : 'Key Not found')
  
# # # initializing values 
# # defd['a'] = 1
  
# # # initializing values 
# # defd['b'] = 2
  
# # # printing value 
# # print ("The value associated with 'a' is : ",end="")
# # print (defd['a'])
  
# # # printing value associated with 'c'
# # print ("The value associated with 'c' is : ",end="")
# # print (defd['c'])

# # 4.
# import collections as col
# #set the default factory with the string 'key not present'
# country_dict = col.defaultdict(lambda: 'Key Not Present')
# country_dict['India'] = 'IN'
# country_dict['Australia'] = 'AU'
# country_dict['Brazil'] = 'BR'
# print(country_dict['Australia'])
# print(country_dict['Canada'])
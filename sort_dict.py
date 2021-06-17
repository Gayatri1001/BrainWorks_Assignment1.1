# # # # # # Ways to sort list of dictionaries by values inPython – Using itemgetter 
# # # # # # 1.
# # # # # ## list of dictionaries
# # # # # dicts = [
# # # # #    {"name" : "John", "salary" : 10000},
# # # # #    {"name" : "Emma", "salary" : 30000},
# # # # #    {"name" : "Harry", "salary" : 15000},
# # # # #    {"name" : "Aslan", "salary" : 10000}
# # # # # ]

# # # # # ## sorting the above list using 'lambda' function
# # # # # ## we can reverse the order by passing 'reverse' as 'True' to 'sorted' method
# # # # # print(sorted(dicts, key = lambda item: item['salary']))

# # # # # 2.
# # # # ## importing itemgetter from the operator
# # # # from operator import itemgetter
# # # # ## list of dictionaries
# # # # dicts = [
# # # #    {"name" : "John", "salary" : 10000},
# # # #    {"name" : "Emma", "salary" : 30000},
# # # #    {"name" : "Harry", "salary" : 15000},
# # # #    {"name" : "Aslan", "salary" : 10000}
# # # # ]

# # # # ## sorting the above list using 'lambda' function
# # # # ## we can reverse the order by passing 'reverse' as 'True' to 'sorted' method
# # # # print(sorted(dicts, key = itemgetter('salary')))

# # # # 3.
# # # from operator import itemgetter
  
# # # # Initializing list of dictionaries
# # # lis = [{ "name" : "Nandini", "age" : 20}, 
# # # { "name" : "Manjeet", "age" : 20 },
# # # { "name" : "Nikhil" , "age" : 19 }]
  
# # # # using sorted and itemgetter to print list sorted by age 
# # # print "The list printed sorting by age: "
# # # print sorted(lis, key=itemgetter('age'))
  
# # # print ("\r")
  
# # # # using sorted and itemgetter to print list sorted by both age and name
# # # # notice that "Manjeet" now comes before "Nandini"
# # # print "The list printed sorting by age and name: "
# # # print sorted(lis, key=itemgetter('age', 'name'))
  
# # # print ("\r")
  
# # # # using sorted and itemgetter to print list sorted by age in descending order
# # # print "The list printed sorting by age in descending order: "
# # # print sorted(lis, key=itemgetter('age'),reverse = True)

# # # 4.
# # # Initializing list of dictionaries
# # lis = [{ "name" : "Nandini", "age" : 20},
# # { "name" : "Manjeet", "age" : 20 },
# # { "name" : "Nikhil" , "age" : 19 }]
 
# # # using sorted and lambda to print list sorted
# # # by age
# # print "The list printed sorting by age: "
# # print sorted(lis, key = lambda i: i['age'])
 
# # print ("\r")
 
# # # using sorted and lambda to print list sorted
# # # by both age and name. Notice that "Manjeet"
# # # now comes before "Nandini"
# # print "The list printed sorting by age and name: "
# # print sorted(lis, key = lambda i: (i['age'], i['name']))
 
# # print ("\r")
 
# # # using sorted and lambda to print list sorted
# # # by age in descending order
# # print "The list printed sorting by age in descending order: "
# # print sorted(lis, key = lambda i: i['age'],reverse=True)

# # 5. 
# markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
# marklist = sorted(markdict.items(), key=lambda x:x[1])
# sortdict = dict(marklist)
# print(sortdict)
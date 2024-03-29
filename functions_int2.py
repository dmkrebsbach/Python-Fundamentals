# # Update Values in Dictionaries and Lists

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# # updates
# x[1][0]=15
# students[0]['last_name']='Bryant'
# sports_directory['soccer'][0]='Andres'
# z[0]['y']=30

# print(x)
# print(students)
# print(sports_directory)
# print(z)




# #Iterate Through a List of Dictionaries
# students = [
#         {
#             'first_name':  'Michael', 
#             'last_name' : 'Jordan'
#         },
#         {
#             'first_name' : 'John', 
#             'last_name' : 'Rosales'
#         },
#         {
#             'first_name' : 'Mark', 
#             'last_name' : 'Guillen'
#         },
#         {
#             'first_name' : 'KB', 
#             'last_name' : 'Tonel'
#         }
#     ]

# def iterateDictionary(list):
#         for names in list:
#             print(names)

# iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel




# #Get Values from a List of Dictionaries
# def iterateDictionary2(first_name, list):
#     for people in list:
#         print (people['first_name'])

# def iterateDictionary3(last_name, list):
#     for people in list:
#         print (people['last_name'])

# iterateDictionary2('first_name', students)
# iterateDictionary3('last_name', students)




# # Iterate Through a Dictionary With List Values

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(dict):
#     for key in dict:
#         print(f"{len(dict[key])} {key}")
#         for value in dict[key]:
#             print(value)

# printInfo(dojo)

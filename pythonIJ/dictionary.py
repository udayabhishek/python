# initialize dictionary

person = {}

# add into dictioary
person['username'] = 'IronMan'
person['f_name'] = "Tony"
person['l_name'] = "Stark"
person['age'] = "25"
person['city'] = "Bangalore"
#
# print(person)
# # update dictionary value using key
# person['city'] = 'LA'
#
# print(person)
#
# # delete key-value pair
#
# del person['age']
# print(person)
#
# # get() method
# # print(person['next_mission'])
# # if key-value is not there in the dictionary then it will give KeyError.So, to
# # solve this prob use get() which will take default value If that key will not
# # be there then default value will return
#
# print(person.get('next_mission', 'Not yet assigned'))
#
#
# # person['next_mission'] = 'Infinity wars'
# # looping
# for item in person.items():
#     print(item) # this will return (key, value) in tuple
#     print(item[0]) #key
#     print(item[1]) #value

# for key, value in person.items():
#     print(f"key: {key}")
#     print(f"value: {value}")

# Looping through keys

for keys in person.keys():
    print(keys)

# Looping through values
for values in person.values():
    print(values.title())
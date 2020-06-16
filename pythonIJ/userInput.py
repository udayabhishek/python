# name = input()
# print(f'\nhi {name}')

# name = input("Please enter your name: ")
# print(f'\nhi {name}')

# age = input("enter your age: ")
# age = int(age)
# print(age)

# age = int(input("enter your age: "))
# print(age)

# num = 1
# while(num<=5):
#     print(num)
#     num += 1


# message = ""
# while(message != 'quit'):
#     message = input("Enter quit to quit: ")
#     print(message)
#
# print("bye")

# using flag
# active = True
# while(active):
#     message = input("Enter quit to quit: ")
#     if message == 'quit':
#         active = False
#     print(message)
#
# print("bye")

# using break
# while True:
#     message = input("Enter quit to quit: ")
#     if message == 'quit':
#         break
#
# print("bye")

# removing all matched item from list
mylist = ['qw','sam', 'joe', 'ram','qw', 'lina', 'jenny','qw', 'peter', 'tony', 'tree', 'qw']
while 'qw' in mylist:
    print('hello')
    mylist.remove('qw')
print(mylist)

# adding user input in dictionary
polling_active = True
response = {}
while (polling_active):
    name = input('please enter you name: ')
    place = input('your favorite place: ')

    response[name] = place

    repeat = input('you want to continue: [y/n]')
    if repeat == 'n':
        polling_active = False

print('--poll result--')
print(response)

for name, place in response.items():
    print(f'{name} wants to go to {place}')


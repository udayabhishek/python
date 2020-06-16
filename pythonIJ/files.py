file_name = 'pi_short'
# with open(file_name) as file_data:
#     contents = file_data.read()
#     print(contents.rstrip())
#     text = ''
#     for lines in contents:
#         text += lines
#         print(text)
# # print(contents)

"""read line by line"""
# with open(file_name) as file_data:
#     for lines in file_data:
#         print(lines, end='')

"""making line from list"""

# with open(file_name) as file_data:
#     lines = file_data.readlines()
#
# text = ''
# for line in lines:
#     # print(line.rstrip())
#     text += line.strip()
#
# print(text)

"""reading milions of line of pi"""

file_name = "pi_long"
with open(file_name) as file_data:
    lines = file_data.readlines()
    print(len(lines))

# text = ''
# for line in lines:
#     text += line
#
# print(f'{text[:100]}')

"""find birthday in pi lines"""
# birthday = input("enter your birthday in ddmmyy: ")
# if birthday in lines:
#     print("yes")
# else:
#     print('no')

"""WRITE TO FILE"""

# file_name = "guest.txt"
# with open(file_name, 'a') as file_object:
#     file_object.write(f"wqwqwq\n")
#     file_object.write(f"dfsdfd\n")
#     file_object.write(f"uytutuy\n")


"""Adding multiple lines to a file"""
# file_name = "guest_book.txt"
# with open(file_name, 'a') as file_object:
#     while True:
#         name = input("enter name: ")
#         print(f"Hi {name}, welcome")
#         file_object.write(f"{name}\n")
#         if name == "q":
#             print("bye")
#             break
#     file_object.close()

textList = ["One", "Two", "Three"]

# with open("myOutFile.txt", "w") as file:
#     for line in textList:
#         name = input("enter name: ")
#         file.write(f'{name}\n')


with open("myOutFile.txt", "a") as file:
    while (True):
        name = input("enter name: ")
        if name == 'q':
            break
        file.write(f'{name}\n')

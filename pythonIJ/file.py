
"""reading milions of line of pi"""

file_name = "pi_long"
with open(file_name) as file_data:
    lines = file_data.readlines()

# text = ''
# for line in lines:
#     text += line
#
# print(f'{text[:100]}')

"""find birthday in pi lines"""
birthday = input("enter your birthday in ddmmyy: ")
if birthday in lines:
    print("yes")
else:
    print('n0')
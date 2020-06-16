import json

# filename = 'username.json'
# with open(filename) as f:
#     username = json.load(f)
#     print(f"Welcome back, {username}. ")


filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Enter username:")
    with open(filename, 'w') as f:
        json.dump(username,f)
        print(f"We will remember when you will be back, {username}")
else:
    print(f"Welcome back, {username}")

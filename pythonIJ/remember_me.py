import json

# username = input("Enter username: ")
# filename = 'username.json'
# with open(filename, 'w') as f:
#     json.dump(username, f)
#     print(f'we will remember you when you will be back, {username}')

def get_new_username():
    """Prompt for new Username"""
    username = input('Enter username:')
    filename = "username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def get_stored_username():
    """get stored username" if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """Greet user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}")
    else:
        username = get_new_username()
        print(f"We will remember you when you will be back, {username}")

greet_user()





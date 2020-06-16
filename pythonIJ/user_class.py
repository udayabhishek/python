class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Info: \nname: {self.first_name} {self.last_name}\nage: {self.age}\nlocation:{self.location}")

    def greet_user(self):
        print(f'hi {self.first_name}, how are you today')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Tony', 'Stark', '30', 'California')
print(user.describe_user())
print(user.greet_user())
for _ in range(5):
    user.increment_login_attempts()
print(user.login_attempts)


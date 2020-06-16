class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name} has serves {self.cuisine_type} cuisine')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')


res = Restaurant('Moritz', 'chicken afgani')
print(res)

print(res.restaurant_name)
print(res.cuisine_type)

print(res.describe_restaurant())
print(res.open_restaurant())

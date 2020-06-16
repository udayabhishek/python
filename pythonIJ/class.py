class Restaurant:
    """Creating restaurant class"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} has serves {self.cuisine_type} cuisine')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open')

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num

class IceCreamStand(Restaurant):
    """Creating child class for Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        # self.flavors = "qwe"
        self.flavour = Flavour()

    def flavors_available(self, flavour):
        print(f'{ics.restaurant_name} has {flavour} ice cream')

class Flavour:
    """Creating Flavour class"""
    def __init__(self, flavour = "mango"):
        self.flavour = flavour

    def get_flavour(self):
        print(f'this restaurant has {self.flavour} available')

ics = IceCreamStand('Moritz', 'chicken afgani')
print(ics.open_restaurant())
print(ics.flavors_available('vanila'))
print(ics.flavour.get_flavour())

# restaurant = Restaurant('Moritz', 'chicken afgani')
# # print(restaurant.restaurant_name)
# # print(restaurant.cuisine_type)
# # print(restaurant.describe_restaurant())
#
# print(f'number of customer served is: {restaurant.number_served}')
# # Modifying attribute value directly
# restaurant.number_served = 10
# print(f'number of customer served is: {restaurant.number_served}')
#
# # modifying attribute value through method
# restaurant.set_number_served(44)
# print(f'number of customer served is: {restaurant.number_served}')
#
# # increment throgh a method
# restaurant.increment_number_served(15)
# print(f'number of customer served is: {restaurant.number_served}')
#
# restaurant.increment_number_served(5)
# print(f'number of customer served is: {restaurant.number_served}')



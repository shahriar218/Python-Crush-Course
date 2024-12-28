class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Our restaurant name is {self.restaurant_name}.")
        print(f"We serve {self.cuisine_type} in our restaurant.")

    def open_restaurant(self):
        print("The restaurant is open at 10 am.")

restaurant = Restaurant("Bangla Hotel", "Buffet")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
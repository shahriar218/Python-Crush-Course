class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Our restaurant name is '{self.restaurant_name}'.")
        print(f"We serve '{self.cuisine_type}' in our restaurant.")

    def open_restaurant(self):
        print("The restaurant is open at 10 am.")

restaurant = Restaurant("Bangla Hotel", "Rice")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# additional description for 3 restaurant
restaurant1 = Restaurant("Khan Snacks", "Biriyani")
restaurant2 = Restaurant("Hajir Biriyani", "Biriyani")
restaurant3 = Restaurant("Swampa Restaurant", "Fast Food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
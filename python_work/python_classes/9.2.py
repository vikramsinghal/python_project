class resturant():

    def __init__(self, resturant_name, cuisine_type, location):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.location = location

    def describe_resturant(self):
        print(f"Name of the resturant is {self.resturant_name}")

    def open_resturant(self):
        print(f"We serve {self.cuisine_type} food!")

    def what_location(self):
        print(f"Welcome to our new location at {self.location}.")

my_resturant = resturant("Cool Resturant!", "American", "Telluride")
my_resturant.describe_resturant()
my_resturant.open_resturant()
my_resturant.what_location()

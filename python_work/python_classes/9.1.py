class resturant():

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print(f"Name of the resturant is {self.resturant_name}")

    def open_resturant(self):
        print(f"We serve {self.cuisine_type} food!")

my_resturant = resturant("Cool Resturant!", "American")
my_resturant.describe_resturant()
my_resturant.open_resturant()

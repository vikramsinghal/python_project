class resturant():

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        print(f"Name of the resturant is {self.resturant_name}")

    def open_resturant(self):
        print(f"We serve {self.cuisine_type} food!")

    def read_number(self):
        print(f"Now serving {self.number_served}")

    def update_number(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number
        print(f"Total number of customer served today {self.number_served}")


my_resturant = resturant("Cool Resturant!", "American")
my_resturant.describe_resturant()
my_resturant.open_resturant()

my_resturant.update_number(112)
my_resturant.read_number()

my_resturant.increment_number_served(1)

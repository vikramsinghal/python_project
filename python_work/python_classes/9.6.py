class resturant():

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print(f"Name of the resturant is {self.resturant_name}")

    def open_resturant(self):
        print(f"We serve {self.cuisine_type} food!")


    class IceCreamStand(resturant):
        def __init__(self, resturant_name, cuisine_type):
            super().__init__(resturant_name, cuisine_type)
            self.flavors = 24

        def ice_cream_flavors(self):
            print(f"We have {self.flavors}, {self.flavors} and {self.flavors}")

my_resturant = IceCreamStand("Cool Resturant!", "American")
print (my_resturant.ice_cream_flavors())

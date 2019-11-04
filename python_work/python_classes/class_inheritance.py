class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        print(f"My new car is {self.make} {self.model} {self.year}!")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

my_tesla = ElectricCar("Tesla", "model s", "2019")
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

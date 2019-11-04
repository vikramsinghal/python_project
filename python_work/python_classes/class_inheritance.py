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

my_tesla = ElectricCar("Tesla", "model s", "2019")
print(my_tesla.get_descriptive_name())

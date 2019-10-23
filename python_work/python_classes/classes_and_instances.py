class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        print(f"My new car is {self.make} {self.model} {self.year}!")
my_new_car = Car("Audi", "Q7", "2019")
my_new_car.get_descriptive_name()

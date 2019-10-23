class Car():
    """docstring for ."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # This line is what different about this class. I didn't have to pass an argument in the init parameters

    def get_descriptive_name(self):
        print(f"My new car is {self.make} {self.model} {self.year}!")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car("Audi", "Q7", "2019")
my_new_car.get_descriptive_name()
my_new_car.read_odometer()

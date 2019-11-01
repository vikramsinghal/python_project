class Car():
    """docstring for ."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print(f"My new car is {self.make} {self.model} {self.year}!")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        self.odometer_reading = milage

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_used_car = Car('Subaru', 'Outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()


my_used_car.increment_odometer(1000)
my_used_car.read_odometer()

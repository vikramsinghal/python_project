class Car(object):
    """docstring for Car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        print(f"I drive a {self.year} {self.make} {self.model}.")

    def get_odometer_reading(self):
        print(f"Car had {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        self.odometer_reading = milage

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_car = Car("Subaru", "Forester", 2019)
my_car.get_descriptive_name()
my_car.get_odometer_reading()

my_car.update_odometer(100)
my_car.get_odometer_reading()

my_car.increment_odometer(2)
my_car.get_odometer_reading()

<<<<<<< HEAD
import time
some_num = int((time.time() * 1000))
print(some_num)
=======
class person():
    """docstring for ."""

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def get_information(self):
        print(f"See below for information about {self.name}")

    def get_name(self):
        print(f"First name is {self.name}")

    def get_age(self):
        print(f"{self.name} is {self.age} years old.")

    def get_city(self):
        print(f"{self.name} lives in {self.city}.")

information = person("Matthew Perry", 34, "New York")

information.get_name()
information.get_age()
information.get_city()
>>>>>>> 7b3d584cbae30ce6ef1b326b3d5e925b2eab001e

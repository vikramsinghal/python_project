class Dog(object):
    """docstring for Dog."""

    def __init__(self, name, age, gender, breed):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed

    def what_breed(self):
        print(f"{self.name} is a {self.breed}.")
    def what_name(self):
        print(f"My dog's name is {self.name}.")
    def what_gender(self):
        print(f"{self.name} is a {self.gender}.")
    def what_age(self):
        print(f"{self.name} is {self.age} years old.")

my_dog = Dog("Kate", 6, "Female", "Corgi")

my_dog.what_breed()
my_dog.what_name()
my_dog.what_gender()
my_dog.what_age()

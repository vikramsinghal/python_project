class Dog():
    """docstring for Dog."""

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def what_name(self):
        print(f"My dog's name is {self.name}.")
    def what_age(self):
        print(f"{self.name} is {self.age} years old.")
    def what_breed(self):
        print(f"{self.name} is {self.breed}.")
my_dog = Dog("Willie", 6, "mix")
my_dog.what_name()
my_dog.what_age()
my_dog.what_breed()

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
#################

class Dog():
    """docstring for Dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} is now rolled over.")

my_dog = Dog("Bruno", 6)

print(f"My Dog's name is {my_dog.name}")
print(f"{my_dog.name} is {my_dog.age} years old.")
my_dog.roll_over()
my_dog.sit()


########### Personalized dog:

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

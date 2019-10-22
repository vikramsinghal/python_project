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

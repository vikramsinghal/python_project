class User():
    """docstring for User."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"Mr.{self.first_name} {self.last_name} is a singer.")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")
my_user = User("Pato", "Banton")

my_user.greet_user()
my_user.describe_user()

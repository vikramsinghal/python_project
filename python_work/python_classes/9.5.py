class User():
    """docstring for User."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = 0

    def describe_user(self):
        print(f"Mr.{self.first_name} {self.last_name} is a singer.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

    def read_login_attempts(self):
        print(f"You have logged in {self.login_attemps} times")

    def increment_login_attempts(self, login):
        self.login_attemps += login

    def reset_login_attempts(self, reset):
        self.login_attemps = reset
        print(f"Resetting your login back to {self.login_attemps}")

my_user = User("Pato", "Banton")

my_user.greet_user()
my_user.describe_user()

my_user.increment_login_attempts(10)
my_user.read_login_attempts()

my_user.reset_login_attempts(0)

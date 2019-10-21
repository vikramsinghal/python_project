def make_pizza(size, *toppings):
    print(f"Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

import make_pizza
pizza.make_pizza(16, "peporini")

#For some reason this file isn't working

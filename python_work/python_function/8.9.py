def make_pizza(size, *toppings):
    print(f'\nYour pizza size is {size}"')
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, "Peporini")

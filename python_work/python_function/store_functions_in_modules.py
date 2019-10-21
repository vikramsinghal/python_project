def pizza(size, *toppings):
    print(f"\nYour {size}-inch pizza is coming with the following toppings:")
    for topping in toppings:
        print("f-{topping}")

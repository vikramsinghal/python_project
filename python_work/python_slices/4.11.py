friend_pizzas = ["canadian bacon", "falafel", "carrot cake"]
friend_pizzas.append("peporoni")
print(friend_pizzas)
new_pizza = friend_pizzas[:]
new_pizza.append("Hawiian Pizza")
print(new_pizza)

for pizza in new_pizza:
    print(f"My favorite pizzas are {pizza.title()}")
print ("\n")
for pizzas in friend_pizzas:
    print(f"My friends favorite pizzas are {pizzas}")

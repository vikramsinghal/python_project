prompt = "\nEnter toppings for your pizza. "
prompt += "\nType 'quit' when you are done. "
toppings = ""
while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"{toppings.title()} has been added to your pizza!")

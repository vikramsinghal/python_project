#Using break to exit a loop

prompt = "\nPlease enter the name of the city you have visited: "
prompt = "\nPlease enter 'quit' when you are done."

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to visit {city.title()}")

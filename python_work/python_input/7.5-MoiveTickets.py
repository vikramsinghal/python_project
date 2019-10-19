prompt = "\nEnter the age to find out the cost of your movie ticket! "
prompt += "\nType quit when you are done! "

active = True
while active:
    age = input(prompt)

    if age == "quit":
        active = False
    elif age == 1:
        print(f"You are {age} year old, you enter free!")

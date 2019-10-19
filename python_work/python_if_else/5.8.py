requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    print(f"Adding extra {requested_topping}")
print("\nFinshed making your pizza.")


#We have now run out of green peppers

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print(f"Unfortunately, we have run out of {requested_topping}")
print("\nFinshed making your pizza.")

print ("<------------->")

#We are going to display each item that is added on the pizza
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print(f"Unfortunately, we have run out of {requested_topping}")
    else:
        print(f"Adding extra {requested_topping}")
print("Finshed making your pizza.")

#Check if the list is empty

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinshed making pizza")
else:
    print ("Are you sure you want a pizza?")


print ("<===========>")
## Working woth multiple lists

available_toppings = ["mushrooms", "green peppers", "extra cheese", "pepproni", "pineapple", "olives",]
requested_toppings = ["mushrooms", "french fries", "extra cheese", "green olives"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print (f"Adding {requested_topping}")
    else:
        print(f"Sorry we don't have {requested_topping}")
print ("Finshed making your pizza")
print ("\n")

#Exercice practice

usernames = ["admin", "Matt", "Jeff", "Jon", "Adam", "Paul", "Jack", "Chad"]
for username in usernames:
    if username == "admin":
        print (f"Hello, {username.title()} would you like to see a status report?")
    else:
        print (f"Hello {username.title()}, thank you for loggin in again.")

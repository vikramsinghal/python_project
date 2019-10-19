available_toppings = ["mushrooms", "green peppers", "extra cheese", "pepproni", "pineapple", "olives",]
requested_toppings = ["mushrooms", "french fries", "extra cheese", "green olives"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print (f"Adding {requested_topping}")
    else:
        print(f"Sorry we don't have {requested_topping}")
print ("Finshed making your pizza")
print ("\n")

current_users = ["matt", "Jeff", "jon", "Adam", "Paul", "Jack", "Chad"]
new_users = ["Jack", "Chad", "Jeff", "Matt", "Banana"]
for new_user in new_users:
    if new_user in current_users:
        print (f"{new_user} will need to enter a new username.")
    else:
        print (f"{new_user} Username is available.")

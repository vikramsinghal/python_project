cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print (car.title())

requested_topping = ["mushrooms", "olives", "tomato"]
print ("ushrooms" in requested_topping)

#banned user list

banned_users = ["andrew", "carolina", "david", "marie"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, allowed to comment if they like.")


# car = 'subaru'
# if car == 'subaru':
#     print ("Is car == 'subaru' ? I predict True.")
#     print (car == 'subaru')
# else:
#     print("\nIs car == 'audi' ? I predict False.")
#     print (car == 'audi')

cars = ["subaru", "Honda", "Toyota", "BMW", "Audi", "Lexus", "VolksWagon", "Ford"]
for car in cars:
    if (car == "Lexus") :
        print (f"\nI like {car}")
    else:
        print (f"Not a fan of {car}")

mode_of_transportation = ["Airplane", "Space Shuttle", "millennium falcon"]

print (f"I would like to own a {mode_of_transportation[2].title()}")
print (f"I would like to own a {mode_of_transportation[1].title()}")
print (f"I would like to own an {mode_of_transportation[0].title()}")




#Pop
mode_of_transportation = ["Airplane", "Space Shuttle", "millennium falcon"]
print (mode_of_transportation)
new_transportation = mode_of_transportation.pop(1).title()
print (new_transportation)
print (mode_of_transportation)
print (f"Last mode of transortation I owned was {new_transportation}")
guest_list = ["jim Carrey", "steve jobs", "Bill gates"]

print (f"Hi {guest_list[0].title()} I would like to invite you over dinner at my house.")
print (f"Hi {guest_list[1].title()} I would like to invite you over dinner at my house.")
print (f"Hi {guest_list[2].title()} I would like to invite you over dinner at my house.")

guest_not_coming = 'steve jobs'
guest_list.remove(guest_not_coming)
print (f"Unfortunately, {guest_not_coming.title()} won't be able to make it.")

guest_list.insert(1, "Taylor Swift")
print (guest_list)

print (f"Hi {guest_list[0].title()} I would like to invite you over dinner at my house.")
print (f"Hi {guest_list[1].title()} I would like to invite you over dinner at my house.")
print (f"Hi {guest_list[2].title()} I would like to invite you over dinner at my house.")

guest_list.insert(0, "Tim Cook")
guest_list.insert(2, "Mark Zukerburg")
guest_list.insert(6, "Banana")
print (guest_list)

print (f"Hi, {guest_list[0].title()} I would like to invite you over dinner at my house.")
print (f"Hi, {guest_list[1].title()} I would like to invite you over dinner at my house.")
print (f"Hi, {guest_list[2].title()} I would like to invite you over dinner at my house.")
print (f"Hi, {guest_list[3].title()} I would like to invite you over dinner at my house.")
print (f"Hi, {guest_list[4].title()} I would like to invite you over dinner at my house.")
print (f"Hi, {guest_list[5].title()} I would like to invite you over dinner at my house.")

print ("I can only invite two people for dinner.")

print (f"I'm sorry I can invite {guest_list.pop()} to dinner")
print (f"I'm sorry I can invite {guest_list.pop()} to dinner")
print (f"I'm sorry I can invite {guest_list.pop()} to dinner")
print (f"I'm sorry I can invite {guest_list.pop()} to dinner")

print ("Got here")

print (f"{guest_list[0]} is still invited")
print (f"{guest_list[1]} is still invited")

del guest_list[1]
print (guest_list)
del guest_list[0]
print (len(guest_list))
multiple_of_ten = input("Enter a number. ")
multiple_of_ten = int(multiple_of_ten)

if multiple_of_ten % 10 == 0:
    print (f"Your number {multiple_of_ten} is a multiple of 10.")
else:
    print(f"Your number {multiple_of_ten} is not a multiple of 10.")

def make_sandwich(type_od_sandwich,*items):
    print(f"\nYour {type_od_sandwich.title()} sandwich is being ordered with the following items:")
    for item in items:
        print(f"- {item}")
make_sandwich("Beef pastrami","Mayo")

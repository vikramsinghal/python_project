# aliens = []
# for alien_number in range(30):
#     new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print(f"Total number of alien: {len(aliens)}")

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t{topping}")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'c#'],
}
for name, languages in favorite_languages.items():
    print(f"{name.title()} favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")

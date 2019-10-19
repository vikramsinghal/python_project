# #Looping through a dictionary
favorite_numbers = {
    'vikram':'1',
    'crystal':'2',
    'abhishek':'3',
    'garima':'4',
    'dad':'5',
    'mom':'6',
}
for name, number in favorite_numbers.items():
    print(f"Name: {name.title()} | Favorite Number: {number}")
for name in favorite_numbers.keys():
    print(f"Name: {name.title()}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print (f"\t{name.title()}, I see you love {language}!")
#Use sort method
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, Thank you for taking the poll!")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for language in favorite_languages.values():
    print (f"{language}")


words = {
    'lists': 'Meaning creating an array and having a lot of things in it.',
    'if': 'This is a condition statement',
    'else': 'This works when if is not true',
    'loops': 'loops help you do the repeatitive task very quickly.',
    'dictionaries': 'dictionaries have key and value pair',
}

for word, meaning in words.items():
    print(f"Key: {word} | Value: {meaning}")
words = {
    'one': '1',
    'two': '2',
    'three': '3',
}
for word, meaning in words.items():
    print(f"Key: {word} | Value: {meaning}")

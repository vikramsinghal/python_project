favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jon': 'objective c',
    'adam': 'swift',
}
friends = ['jon', 'adam']
for names in favorite_languages:
    print(f"Hi, {names.title()}")

    if names in friends:
        poll = favorite_languages[names].title()
        print(f"Hi {names}, I see that you didn't take {poll}")

#
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name.title()}, I see you like {language}!")

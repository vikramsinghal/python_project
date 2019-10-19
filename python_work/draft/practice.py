<<<<<<< HEAD
person = {
    'first_name':'Vikram',
    'last_name':'Singhal',
    'City':'Boulder',
}

person_info = person
print(f"First name is: {person_info['first_name']}")
print(f"Last name is: {person_info['last_name']}")
print(f"City is: {person_info['City']}")

server = {
    '10.1.11.139': 'qadenweb73',
    '10.1.11.140': 'qadenweb72',
}
enter_ip = input("Enter IP here: ")
for ip_address, web_server in server.items():
    web_server = enter_ip
    if enter_ip in server:
        print(f"{enter_ip} belongs to {server[web_server]}")
        break
    else:
        print("Please enter a valid IP.")
        break



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
=======
num1 = "36"
num2 = "5"
total = (num1 + num2)
total2 = (num2*5)
print (total2)
>>>>>>> vikram_macbook

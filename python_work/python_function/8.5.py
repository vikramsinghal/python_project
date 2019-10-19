# def describe_city(city_name, country_name):
#     print(f"{city_name} is in {country_name}")
# describe_city("Boulder", "United States")
#
# def describe_city(city_name, country_name):
#     print(f"{city_name} is in {country_name}")
# describe_city("Oslo", "Norway")
#

# def describe_city(city_name, country_name="Norway"):
#     print(f"{city_name} is in {country_name}")
# describe_city("Ouray")

#Returning a simple value

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = get_formatted_name("jimi", "hendrix")
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=""):
#     if middle_name:
#         full_name = f"{first_name} {last_name} {middle_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name("Barack", "Husain", "Obama")
# print (musician)
#
#
# def build_person(first_name, last_name):
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print (musician)
#

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at anytime to quit)")

f_name = input('Fist name: ')
if f_name == 'q':
    break
l_name = input('Last name:')
if l_name == 'q':
    break
formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}")

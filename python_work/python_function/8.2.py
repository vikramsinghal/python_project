# ask = "What's your favorite book? "
# response = input(ask)
# def favorite_book(title):
#     print(f"Your favorite books is {title}")
# favorite_book(response)

# def describe_pet(animal_type, pet_name):
#     print(f"My animal's is a: {animal_type} and his name is: {pet_name}")
# describe_pet("Hamster","Harry")
# describe_pet("Cat","Gidget")
#
question_one = "What is your animal name? "
response_one = input(question_one)
question_two = "What kind of animal is he? "
response_two = input(question_two)

def describe_pet(pet_name, kind):
    print(f"My animal name is: {pet_name}")
    print(f"My animal name is: {kind}")
describe_pet(response_one, response_two)

def describe_pet(pet_name, animal_type ="dog"):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet(pet_name = "Willie")

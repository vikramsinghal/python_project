words = {
    'lists': 'Meaning creating an array and having a lot of things in it.',
    'if': 'This is a condition statement',
    'else': 'This works when if is not true',
    'loops': 'loops help you do the repeatitive task very quickly.',
    'dictionaries': 'dictionaries have key and value pair',
}
programming_words = words
print(f"Here's the meaning of having a 'List' in python language: {programming_words['lists']}")
print(f"Here's the meaning of having a 'if' statement in python language: {programming_words['if']}")
print(f"Here's the meaning of having a 'else' statement in python language: {programming_words['else']}")
print(f"Here's the meaning of having a 'loops' in python language: {programming_words['loops']}")
print(f"Here's the meaning of having a 'dictionaries' in python language: {programming_words['dictionaries']}")

for key, value in words.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

server = {
    '10.1.11.139': 'qadenweb73',
    '10.1.11.140': 'qadenweb72',
}
for ip_address, web_server in server.items():
    enter_ip = input("Enter IP here: ")
    server_ip = enter_ip
    print("banana")

prompt = "\n Type something and I will repeat. "
prompt = "\n Type 'exit' to exit out of the program. "
message = ""

active = True
while active:
    message = input(prompt)

    if message == 'exit':
        active = False
    else:
        print(message)

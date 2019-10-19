# def greet_name(names):
# 	for name in names:
# 		message = f"Hi, {name.title()}!"
# 		print (message)
# username = ['Vikram', 'crystal', 'abhishek']
# greet_name(username)
#

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print (f"Printing model: {current_design}")
	completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_models in completed_models:
	print(completed_models)

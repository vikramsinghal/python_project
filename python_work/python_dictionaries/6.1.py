alien_0 = {'color': 'green', 'points': 5}
print (alien_0['color'])
print (alien_0['points'])
print (alien_0['speed'])



alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] =25
print(alien_0)

alien_0 = {}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

alien_0 ={'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New Position: {alien_0['x_position']}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

print(favorite_languages['sarah'])

person = {
    'first_name':'Vikram',
    'last_name':'Singhal',
    'City':'Boulder',
}
print(person['first_name'])
print(person['last_name'])
print(person['City'])

#person_info = person
print(f"First name is: {person['first_name']}")
print(f"Last name is: {person['last_name']}")
print(f"City is: {person['City']}")

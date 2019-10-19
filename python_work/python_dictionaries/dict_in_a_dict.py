users = {
  'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'banana': 'fruit'
  },
  'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'place': 'paris',
  },
}
for username, user_info in users.items():
    print(f"Username: {user_info}")
    full_name = f"{user_info['first']} {user_info['last'] {user_info['banana']}"
    #location = user_info['place']

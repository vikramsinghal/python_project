def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Banana', 'Orange', location = 'Mars', temprature= 'cold and hot', space_ship= 'Falcon')
print(user_profile)

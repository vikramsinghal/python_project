def car(manufacturer, model, **more_info):
    more_info['manufacturer'] = manufacturer
    more_info['model'] = model
    return more_info
car_info = car('Honda', 'Civic', color='Silver', four_wheel_drive='No')
print(car_info)

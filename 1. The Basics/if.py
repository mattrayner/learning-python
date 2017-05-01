available_toppings = ['extra cheese', 'mushrooms', 'pepperoni', 'rocket']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if available_toppings and requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print('Adding ' + requested_topping + '.')
        elif requested_topping == 'Nothing':
            print('Garnishing with nothing.')
        else:
            print('Sorry, we\'re out of '+requested_topping)
else:
    print('There needs to be some available toppings, and some requested toppings')

print('\nFinished making pizza!')
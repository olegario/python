import os
os.system('clear')

'''first_name = 'Olegario'
last_name = 'Ballester'

print(f'Hello World, {first_name}')
print(type(first_name))'''


'''Diccionarios'''

fav_pizzas = {
	'John':'Peperoni',
	'Tim' : 'Mushrooms',
	'Mary' : 'Cheese'
}
for key, value in fav_pizzas.items():
	print(f'{key} --> {value}.')
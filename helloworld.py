############################
# Autor: Olegario Ballester
############################

import os
os.system('clear')

'''first_name = 'Olegario'
last_name = 'Ballester'

print(f'Hello World, {first_name}')
print(type(first_name))'''


'''Diccionarios'''

'''fav_pizzas = {
	'John':'Peperoni',
	'Tim' : 'Mushrooms',
	'Mary' : 'Cheese'
}
for key, value in fav_pizzas.items():
	print(f'{key} --> {value}.')
'''
''' Fizzbuzz
	%3 Fizz
	%5 buzz
	%3 & %5 Fizzbuzz'''

count_3 = 0
count_5 = 0
count_3_5 = 0
count = 0


for i in range(1,101):
	if i%3 == 0 and i%5==0:
		count_3_5 += 1
		print(f'{i} Fizzbuzz')
	elif i%5 == 0:
		count_5 += 1
		print(f'{i} buzz')
	elif i%3==0 :
		count_3 += 1
		print(f'{i} Fizz')
	else:
		count += 1
		print(f'{i}')

print(f' Fizz: {count_3}\nbuzz: {count_5}\nFizzbuzz: {count_3_5}\nResto:{count} ')
		
		

############################
# Autor: Olegario Ballester
############################

import os
os.system('clear')
import sqlite3

#conectar con la base datos
conn = sqlite3.connect('customer.db')
# crear cursor
c = conn.cursor()

# crear tabla
'''c.execute("""CREATE TABLE customer
			(
			first_name text,
			last_name text,
			email text
			)
			""")'''
#c.execute("INSERT INTO customer VALUES ('Olegario','Ballester','olegario.ballester@gmail.com')")

c.execute("SELECT * FROM customer")
items =c.fetchall()

for item in items:
	print(item[2])
for item in items:
	print(f'{item[0]} {item[1]} has the mail: {item[2]}.')


conn.commit()








# cerrar conexion
conn.close()
# Ejercicio 7.1: Segundos vividos
# Escribí una función a la que le pasás tu fecha de 
# nacimiento como cadena en formato 'dd/mm/AAAA' 
# (día, mes, año con 2, 2 y 4 dígitos, separados con barras normales) 
# y te devuelve la cantidad de segundos que viviste (asumiendo que naciste a las 00:00hs 
# de tu fecha de nacimiento).

# Guardá este código en el archivo vida.py.

import datetime

def get_lifespan_in_seconds(birthday):
    birthday_datetime = datetime.datetime.strptime(birthday, '%d/%m/%Y')
    
    return (datetime.datetime.now() - birthday_datetime).total_seconds()

print(get_lifespan_in_seconds('17/01/1997'))
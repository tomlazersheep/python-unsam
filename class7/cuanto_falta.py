# Ejercicio 7.2: Cuánto falta
# Un conocido canal Argentino tiene por costumbre anunciar la 
# cantidad de días que faltan para la próxima primavera.
# Escribí un programa que asista a los técnicos del canal indicándoles,
# al correr el programa el número que deben poner en la placa.

import datetime

today = datetime.date.today()
spring_day_this_year = datetime.date(today.year, 9, 21)
spring_day_next_year = datetime.date(today.year+1, 9, 21)

days_to_this_year = spring_day_next_year - today

if (days_to_this_year) < datetime.timedelta(0):
    print(days_to_this_year)
else:
    print(spring_day_next_year - today)

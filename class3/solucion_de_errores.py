# solucion_de_errores.py
# Ejercicios de errores en el código
# %%
# Ejercicio 3.1: Semántica
# ¿Anda bien en todos los casos de testeo?
# Estaba solamente mirando la primera letra


from pprint import pprint
import csv
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))


# %%
# Ejercicio 3.2.
# Comentario: mal indentado, faltaban todos los : y
# había un operador de asignación (=) en el if.
# Además retornaba "Falso" que no estaba definido

def tiene_a2(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


print(tiene_a2('UNSAM 2020'))
print(tiene_a2('La novela 1984 de George Orwell'))

# %%
# Ejercicio 3.3. Función tiene_uno()
# Comentario: No se tenía en cuenta que el parámetro
# podía ser un número, con str() se lo fuerza a ser un
# string (es más eficiente que usar un try-except)


def tiene_uno(expresion):
  expresionString = str(expresion)
  n = len(expresionString)
  i = 0
  tiene = False
  while (i < n) and not tiene:
    if expresionString[i] == '1':
      tiene = True
    i += 1
  return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

# %%
# Ejercicio 3.4: Alcances
# La siguiente suma no da lo que debería:
# No se retornaba la suma, el retorno de la función era 
# None, que es un valor indefinido

def suma(a, b):
  return (a + b)

a = 2
b = 3
c = suma(a, b)
print(f"La suma da {a} + {b} = {c}")

#%%
# Ejercicio 3.5: Pisando memoria
# El siguiente ejemplo usa el dataset de la clase
# anterior, pero no lo imprime como corresponde, 
# ¿podés determinar por qué y explicarlo brevemente en la 
# versión corregida?
# los pares key-value que se ponen en registro tienen
# como values a valores de fila, pero lo que queda
# appendeado en el diccionario es un puntero al valor
# de fila, que cambia en cada ciclo, entonces nos quedamos
# con el último valor que toma fila en todos lados.
# Todos los valores guardados son direcciones que apuntan
# al mismo lugar, que cambia con cada iteración. Al bajar
# la declaración de la variable adentro del for, la descarto
# y vuelvo a crear en cada ciclo, eliminando el problema.

import csv 
from pprint import pprint 

def leer_camion(nombre_archivo):
  camion = []
  with open(nombre_archivo, "rt") as f:
    filas = csv.reader(f)
    encabezado = next(filas)
    for fila in filas:
      registro = {}
      registro[encabezado[0]] = fila[0]
      registro[encabezado[1]] = int(fila[1])
      registro[encabezado[2]] = float(fila[2])
      camion.append(registro)
  return camion


camion = leer_camion("../Data/camion.csv")
pprint(camion)

# %%

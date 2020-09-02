import numpy as np
import random


# Ejercicio 4.15: Crear
# Implementá la función crear_album(figus_total) que devuelve un álbum(vector)
# vacío con figus_total espacios para pegar figuritas.

def crear_album(figus_total):
  return np.zeros(figus_total)


# Ejercicio 4.16: Incompleto
# ¿Cuál sería el comando de Python que nos dice si hay al menos
#  un cero en el vector que representa el álbum? ¿Qué significa que
#  haya al menos un cero en nuestro vector?

# Implemente la función album_incompleto(A) que recibe un vector y devuelve
#  True si el vector contiene el elemento 0. En
#  el caso en que no haya ceros debe devolver False.

# Estas funciones son tan sencillas - -cada una puede escribirse en
#  una sola línea-- que podría ponerse directamente esa línea cada vez que queremos llamar
#  a la función. Sin embargo, en esta etapa nos parece conveniente que organices el
#  código en funciones, por más que sean sencillas.

def album_incompleto(A):
  return not(np.count_nonzero(A!=0) == A.size)


# Ejercicio 4.17: Comprar
# Alguna de las funciones que introdujimos en la Sección 4.2 sirve
#  para devolver un número entero aleatorio dentro de un rango(¿cuál era?).
#  Implementá una función comprar_figu(figus_total) que reciba el número total de 
# figuritas que tiene el álbum(dado por el parámetro figus_total) y devuelva
#  un número entero aleatorio que representa la figurita que nos tocó.

def comprar_figu(figus_total):
  return random.randint(0,figus_total)


# Ejercicio 4.18: Cantidad de compras
# Implementá la función cuantas_figus(figus_total) que, dado el tamaño del
# álbum(figus_total), genere un álbum nuevo, simule su llenado y devuelva la
# cantidad de figuritas que se debieron comprar para completarlo.

def cuantas_figus(figus_total):
  album = crear_album(figus_total)
  compras = 0
  while album_incompleto(album):
    album[comprar_figu(figus_total) - 1] = 1
    compras += 1
  return compras

n = 10000
resultados = []
album_size = 6
for i in range(n):
  resultados.append(cuantas_figus(album_size))
print(f'En {n} album de {album_size} figuritas se compra en promedio {np.mean(np.array(resultados))}')


# Ejercicio 4.20:
# Calculá n_repeticiones = 100 veces la función cuantas_figus(figus_total=670) 
# y guardá los resultados obtenidos en cada repetición en una lista. Con los resultados  
# obtenidos estimá cuántas figuritas hay que comprar, en promedio, para completar   
# el álbum(de 670 figuritas).
n_repeticiones = 100
album_size = 670
results = []

for i in range(n_repeticiones):
  results.append(cuantas_figus(album_size))
print(f'En {n_repeticiones} album de {album_size} figuritas se compra en promedio {np.mean(np.array(results))}')


# Ejercicio 4.22:
# Implementá una función comprar_paquete(figus_total, figus_paquete)
# que, dado el tamaño del álbum(figus_total) y la cantidad
# de figuritas por paquete(figus_paquete), genere un paquete(vector) 
# de figuritas al azar.

def comprar_paquete(figus_total, figus_paquete):
  figus = []
  for _ in range(figus_paquete):
    figus.append(random.randint(0,figus_total))
  return np.array(figus)


# Ejercicio 4.23:
# Implementá una función cuantos_paquetes(figus_total, figus_paquete) que
# dado el tamaño del álbum y la cantidad de figus por paquete, genere
# un álbum nuevo, simule su llenado y devuelva cuántos paquetes se
# debieron comprar para completarlo.

def cuantos_paquetes(figus_total, figus_paquete):
  album = crear_album(figus_total)
  paquetes = 0
  while album_incompleto(album):
    paquetes += 1
    for figu in comprar_paquete(figus_total, figus_paquete):
      album[figu - 1] = 1
  return paquetes


# Ejercicio 4.24:
# Calculá n_repeticiones = 100 veces la función cuantos_paquetes, utilizando 
# figus_total = 670, figus_paquete = 5. Guarda los resultados obtenidos en una lista
#  y calculá su promedio. Si te da la compu, hacelo con 1000 repeticiones.
n_repeticiones = 1000
figus_total = 670
figus_paquete = 5
results = []

for i in range(n_repeticiones):
  results.append(cuantos_paquetes(figus_total, figus_paquete))
print(f'En {n_repeticiones} album de {figus_total} figuritas se compra en promedio {np.mean(np.array(results))}')


# Ejercicio 4.25:
# Utilizando lo implementado en el ítem anterior, estimá
# la probabilidad de completar el álbum con 850 paquetes o menos.

# del anterior tengo n_repeticiones y results con lo que sale de cada repe, voy a quedarme con los
# resultados menores a 850 y dividir por n_repeticiones

np_results = np.array(results)

resultados_menos_850 = np_results[np_results <= 850]

proba = resultados_menos_850.size / n_repeticiones

print(f'La probabilidad de llenar el album con 850 o menos paquetes es de {proba}')



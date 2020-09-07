# Usando experimento_secuencial_promedio(lista,m,k) como 
# base, escribí una función experimento_binario_promedio(lista,m,k)
# que cuente la cantidad de comparaciones que realiza en promedio
# (entre k experimentos elementales) la búsqueda binaria sobre la 
# lista pasada como parámetro.
# Graficá los resultados de estos experimentos para listas de largo entre 1 y 256.
# Graficá ambas curvas en una misma figura, nombrando adecuadamente las curvas,
# los ejes y la figura completa.
# ¿Qué observas en estos gráficos? ¿Qué podés decir sobre la complejida 
# de cada algoritmo?
import matplotlib.pyplot as plt
import numpy as np
import random

k = 1000
m = 1000000
n = 100

def generar_elemento(m):
  return random.randint(0, m-1)

def generar_lista(n, m):
  l = random.sample(range(m), k=n)
  l.sort()
  return l


def busqueda_secuencial_(lista, e):
  '''Si e está en la lista devuelve el índice de su primer aparición, 
  de lo contrario devuelve -1.
  '''
  comps = 0  # inicializo en cero la cantidad de comparaciones
  pos = -1
  for i, z in enumerate(lista):
    comps += 1  # sumo la comparación que estoy por hacer
    if z == e:
      pos = i
      break
  return pos, comps




def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for _ in range(k):
        e = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista, e)[1]

    comps_prom = comps_tot / k
    return comps_prom



def experimento_binario_promedio(lista, m, k):
  comps_tot = 0
  for _ in range(k):
    e = generar_elemento(m)
    comps_tot += busqueda_binaria_(lista, e)[1]

  comps_prom = comps_tot / k
  return comps_prom

def busqueda_binaria_(lista,x):
  izq = 0
  der = len(lista) - 1
  comps = 0
  pos = None
  while izq <= der:
    comps += 1
    medio = (izq + der) // 2
    comps += 1
    if lista[medio] == x:
      pos = medio     # elemento encontrado!
    comps += 1
    if lista[medio] > x:
      der = medio - 1  # descarto mitad derecha
    else:               # if lista[medio] < x:
      izq = medio + 1  # descarto mitad izquierda
  comps += 1
  if pos == None:
    return izq, comps
  return pos, comps


largos = np.arange(256)+1  # estos son los largos de listas que voy a usar
# aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
comps_sec_promedio = np.zeros(256)

for i, n in enumerate(largos):
    lista = generar_lista(n, m)  # genero lista de largo n
    comps_sec_promedio[i] = experimento_secuencial_promedio(lista, m, k)

comps_bin_promedio = np.zeros(256)

for i, n in enumerate(largos):
    lista = generar_lista(n, m)  # genero lista de largo n
    comps_bin_promedio[i] = experimento_binario_promedio(lista, m, k)


#ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos, comps_sec_promedio, label='Búsqueda Secuencial')
plt.plot(largos, comps_bin_promedio, label='Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()


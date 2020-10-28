import random

def ord_burbujeo(lista):
  lista_copy = lista.copy()
  steps = 0
  for _ in lista_copy:
    for j, _ in enumerate(lista_copy[:-1]):
      steps += 1
      if lista_copy[j] > lista_copy[j+1]:
        aux = lista_copy[j]
        lista_copy[j] = lista_copy[j+1]
        lista_copy[j+1] = aux
  return lista_copy, steps

def generar_lista(N):
  lista = []
  for _ in range(N):
    lista.append(random.randint(1,1000))
  return lista


def ord_insercion(lista):
  """Ordena una lista de elementos según el método de inserción.
      Pre: los elementos de la lista deben ser comparables.
      Post: la lista está ordenada."""
  steps = 0
  lista_aux = lista.copy()
  for i in range(len(lista_aux) - 1):
    # Si el elemento de la posición i+1 está desordenado respecto
    # al de la posición i, reubicarlo dentro del segmento [0:i]
    steps += 1
    if lista_aux[i + 1] < lista_aux[i]:
      reubicar(lista_aux, i + 1,steps)
    print("DEBUG: ", lista_aux, steps)
  return lista_aux, steps


def reubicar(lista, p,steps):
  """Reubica al elemento que está en la posición p de la lista
      dentro del segmento [0:p-1].
      Pre: p tiene que ser una posicion válida de lista."""
  v = lista[p]

  # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
  # encontrar la posición j tal que lista[j-1] <= v < lista[j].
  j = p
  while j > 0 and v < lista[j - 1]:
    # Desplazar los elementos hacia la derecha, dejando lugar
    # para insertar el elemento v donde corresponda.
    steps += 3
    lista[j] = lista[j - 1]
    j -= 1

  lista[j] = v


def ord_seleccion(lista):
  """Ordena una lista de elementos según el método de selección.
      Pre: los elementos de la lista deben ser comparables.
      Post: la lista está ordenada."""
  pasos = 0
  lista_aux = lista.copy()

  # posición final del segmento a tratar
  n = len(lista_aux) - 1

  # mientras haya al menos 2 elementos para ordenar
  while n > 0:
    # posición del mayor valor del segmento
    p,pasos = buscar_max(lista_aux, 0, n, pasos)

    # intercambiar el valor que está en p con el valor que
    # está en la última posición del segmento
    lista_aux[p], lista_aux[n] = lista_aux[n], lista_aux[p]
    print("DEBUG: ", p, n, lista_aux, pasos)

    # reducir el segmento en 1
    n = n - 1
  return lista_aux,pasos


def buscar_max(lista_aux, a, b, pasos):
  """Devuelve la posición del máximo elemento en un segmento de
      lista_aux de elementos comparables.
      La lista_aux no debe ser vacía.
      a y b son las posiciones inicial y final del segmento"""

  pos_max = a
  for i in range(a + 1, b + 1):
    pasos += 1
    if lista_aux[i] > lista_aux[pos_max]:
      pos_max = i
  return pos_max,pasos

N = range(1,256)
resultados_sele = []
resultados_inse = []
resultados_burb = []

for n in N:
  lista_p_ordenar = generar_lista(n)
  resultados_sele.append(ord_seleccion(lista_p_ordenar))
  resultados_inse.append(ord_insercion(lista_p_ordenar))
  resultados_burb.append(ord_burbujeo(lista_p_ordenar))

comparaciones_seleccion = [res_n[1] for res_n in resultados_sele]
comparaciones_insercion = [res_n[1] for res_n in resultados_inse]
comparaciones_burbujeo = [res_n[1] for res_n in resultados_burb]

print("comparaciones promedio seleccion: ", sum(comparaciones_seleccion)/len(comparaciones_seleccion))

print("comparaciones promedio inserción: ", sum(comparaciones_insercion)/len(comparaciones_insercion))

print("comparaciones promedio burbujeo: ", sum(comparaciones_burbujeo)/len(comparaciones_burbujeo))

import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({'x_axis':N, 'seleccion':comparaciones_seleccion, 'insercion':comparaciones_insercion,'burbujeo':comparaciones_burbujeo})

data.plot(x='x_axis',y=['seleccion','insercion','burbujeo'], color=['red','green','blue'])
plt.show()
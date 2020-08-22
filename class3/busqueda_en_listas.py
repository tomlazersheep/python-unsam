# escribir una función buscar_u_elemento() que reciba una lista y un
# elemento y devuelva la posición de la última aparición de ese elemento
# en la lista (o -1 si el elemento no pertenece a la lista).
def buscar_u_elemento(lista, el):
  foundElIndex = -1
  for i,listEl in enumerate(lista):
    if listEl == el:
      foundElIndex = i
  return foundElIndex


args = [([1, 2, 3, 2, 3, 4], 1),
        ([1, 2, 3, 2, 3, 4], 2),
        ([1, 2, 3, 2, 3, 4], 3),
        ([1, 2, 3, 2, 3, 4], 5)]

print('buscar_u_elemento')
for arg in args:
  print(f'{arg} --> {buscar_u_elemento(arg[0],arg[1])}')
print('')

# buscar_n_elemento() que reciba una lista y un elemento
# y devuelva la cantidad de veces que aparece el elemento en la lista
# Probá también esta función con algunos ejemplos.
def buscar_n_elemento(lista, el):
  accu = 0
  for listItem in lista:
    if listItem == el:
      accu += 1
  return accu


print('buscar_n_elemento')
for arg in args:
  print(f'{arg} --> {buscar_n_elemento(arg[0],arg[1])}')
print('')

# una función maximo() que busque el valor máximo de una lista 
# de números positivos. Python tiene el comando max que ya hace esto,
# pero como práctica te propomenos que completes el siguiente código:
def maximo(lista):
  '''
  Devuelve el máximo de una lista, 
  la lista debe ser no vacía y de números positivos.
  '''
  # m guarda el máximo de los elementos a medida que recorro la lista.
  maxValue = lista[0] 
  for listElement in lista:  # Recorro la lista y voy guardando el mayor
    if listElement > maxValue:
      maxValue = listElement
  return maxValue


args = [[1, 2, 7, 2, 3, 4],
        [1, 2, 3, 4],
        [-5, 4],
        [-5, -4]]

print('maximo')
for arg in args:
  print(f'{arg} --> {maximo(arg)}')
print('')

def minimo(lista):
  minValue = lista[0]
  for listElement in lista:
    if listElement < minValue:
      minValue = listElement
  return minValue


print('minimo')
for arg in args:
  print(f'{arg} --> {minimo(arg)}')
print('')



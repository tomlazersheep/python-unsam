# Ejercicio 3.18: Lectura de todos los árboles
# Basándote en la función leer_parque(nombre_archivo, parque)
# del Ejercicio 2.22, escribí otra leer_arboles(nombre_archivo)
# que lea el archivo indicado y devuelva una lista de 
# diccionarios con la información de todos los árboles en el archivo.
# La función debe devolver una lista conteniendo un diccionario por cada árbol con todos los datos.

# Vamos a llamar arboleda a esta lista.
import csv
def leer_arboles(nombre_archivo):
  arboleda = []
  with open(nombre_archivo) as rawfile:
    datafile = csv.reader(rawfile)
    headers = next(datafile)
    for line in datafile:
      arboleda.append(dict(zip(headers,line)))
  return arboleda

# print(leer_arboles('../Data/arbolado-en-espacios-verdes.csv'))


# Ejercicio 3.19: Lista de altos de Jacarandá
# Usando comprensión de listas y la variable arboleda podés por
# ejemplo armar la lista de la altura de los árboles.

jacarandaHeights = [int(tree['altura_tot']) for tree in leer_arboles(
    '../Data/arbolado-en-espacios-verdes.csv') if tree['nombre_com'] == 'Jacarandá']

# print(jacarandaHeights)

# Ejercicio 3.20: Lista de altos y diámetros de Jacarandá
# En el ejercicio anterior usaste una sola linea para seleccionar las alturas
# de los Jacarandás en parques porteños. Ahora te proponemos que armes una
# nueva lista que tenga pares(tuplas de longitud 2) conteniendo no solo el
# alto sino también el diámetro de cada Jacarandá en la lista.


jacarandaDiameters = [int(tree['diametro']) for tree in leer_arboles(
  '../Data/arbolado-en-espacios-verdes.csv') if tree['nombre_com'] == 'Jacarandá']

jacarandaData = []

for data in zip(jacarandaHeights,jacarandaDiameters):
  jacarandaData.append(tuple(data))

print(jacarandaData)


# Ejercicio 3.21: Diccionario con medidas

# Te pedimos que armes un diccionario en el que estas especies sean las claves y los valores 
# asociados sean los datos que generaste en el ejercicio anterior. Más aún, organizá tu código
# dentro de una función medidas_de_especies(especies, arboleda) que recibe una lista de
# nombres de especies y una lista como la del Ejercicio 3.18 y devuelve un diccionario
# cuyas claves son estas especies y sus valores asociados sean las medidas 
# generadas en el ejercicio anterior.

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
  medidasDeEspecies = {}
  for especie in especies:
    height = [int(tree['altura_tot'])
              for tree in arboleda if tree['nombre_com'] == especie]
    diameter = [int(tree['diametro'])
              for tree in arboleda if tree['nombre_com'] == especie]
    data = []
    for dataset in tuple(zip(height,diameter)):
      data.append(dataset)
    medidasDeEspecies[especie] = data
  return medidasDeEspecies


print(medidas_de_especies(especies, leer_arboles(
    '../Data/arbolado-en-espacios-verdes.csv')))


# imports
import csv
from collections import Counter

# Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una 
# lista de diccionarios con la información del parque especificado. La función debe devolver, en una
# lista un diccionario con todos los datos por cada árbol del parque elegido (recordá que cada fila del 
# csv es un árbol).
# long,lat,id_arbol,altura_tot,diametro,inclinacio,id_especie,nombre_com,nombre_cie,tipo_folla,espacio_ve,ubicacion,nombre_fam,nombre_gen,origen,coord_x,coord_y
# -58.4775636069,-34.6450145297,1,6,35,0,53,Washingtonia (Palmera washingtonia),Washingtonia filifera,Palmera,"AVELLANEDA, NICOLÁS, Pres.","DIRECTORIO, AV. - LACARRA, AV. - MONTE -  AUTOPISTA PERITO MORENO (AU 6) - AMEGHINO, FLORENTINO, DR.",Arecaceas,Washingtonia,Exótico,98692.30571900001,98253.300738

def leer_parque(filename, parque):
  try:
    fileRaw = open(filename)
  except:
    return 'No se encuentra el archivo :('
  fileCsv = csv.reader(fileRaw)
  headers = next(fileCsv)
  parkTreesList = []
  for tree in fileCsv:
    treeFormat = dict(zip(headers,tree))
    if treeFormat['espacio_ve'] == parque:
      parkTreesList.append(treeFormat)
  return parkTreesList


# Escribí una función especies(lista_arboles) que tome una lista
#  de árboles como la generada en el ejercicio anterior y devuelva el conjunto de
#  especies(la columna 'nombre_com' del archivo) que figuran en la lista.
def especies(lista_arboles):
  species = []
  for tree in lista_arboles:
    species.append(tree['nombre_com'])
  return set(species)


# Usando contadores como en el Ejercicio 2.21, escribí una función contar_ejemplares(lista_arboles)
# que, dada una lista como la que generada con leer_parque(), devuelva un diccionario en el que las
# especies (recordá, es la columna 'nombre_com' del archivo) sean las claves 
# y tengan como valores asociados la cantidad de ejemplares en esa especie en la lista dada.
def contar_ejemplares(lista_arboles):
  treesCounter = Counter()
  for arbol in lista_arboles:
    treesCounter[arbol['nombre_com']] += 1
  return treesCounter


#combiná esta función con leer_parque() y con el método most_common() para informar las cinco
#  especies más frecuentes en cada uno de los siguientes parques:
parks = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO', 'PEREYRA, LEONARDO']

def get5MostCommon(park):
  return contar_ejemplares(leer_parque('../Data/arbolado-en-espacios-verdes.csv', park)).most_common(5)

mostCommons = []
for park in parks:
  mostCommons.append(dict(get5MostCommon(park)))
mostCommonsPerPark = dict(zip(parks,mostCommons))

for park in mostCommonsPerPark:
  print(park)
  for tree in mostCommonsPerPark[park]:
    print(tree, mostCommonsPerPark[park][tree])


# dada una lista de árboles como la anterior y una especie de árbol (un valor de la columna 
# 'nombre_com' del archivo), devuelva una lista con las alturas (columna 'altura_tot') de 
# los ejemplares de esa especie en la lista.
def obtener_alturas(lista_arboles, especie):
  heights = []
  for tree in lista_arboles:
    if tree['nombre_com'] == especie:
      heights.append(float(tree['altura_tot']))
  return heights

for park in parks:

  treeHeights = obtener_alturas(leer_parque(
    '../Data/arbolado-en-espacios-verdes.csv', park), 'Jacarandá')
  print(f'En el parque: {park}:')
  print('lista de alturas de Jacarandá: ', treeHeights)
  print('Maxima altura de Jacarandá: ', max(treeHeights))
  medianTreeHeights = 0
  for height in treeHeights:
    medianTreeHeights+= height

  medianTreeHeights /= len(treeHeights)
  print(f'Promedio altura de Jacarandá: ', medianTreeHeights)
  print(' ')

# Ejercicio 2.26: Inclinación promedio por especie de una lista
# Escribí una función obtener_inclinaciones(lista_arboles, especie) que, dada una especie de
# árbol y una lista de árboles como la anterior, devuelva una lista con las
# inclinaciones(columna 'inclinacio') de los ejemplares de esa especie.
def obtener_inclinaciones(lista_arboles, especie):
  angles = []
  for tree in lista_arboles:
      if tree['nombre_com'] == especie:
        angles.append(float(tree['inclinacio']))
  return angles


for park in parks:
  treeList = leer_parque(
    '../Data/arbolado-en-espacios-verdes.csv', park)
  angles = obtener_inclinaciones(treeList,'Jacarandá')
  medianAngle = 0
  for angle in angles:
    medianAngle+= angle
  medianAngle /= len(angles)
  print(f'La inclinación promedio del arbol Jacarandá en el parque {park} es: {medianAngle}')


# Ejercicio 2.27: Especie con el ejemplar más inclinado
# Combinando la función especies() con obtener_inclinaciones() escribí una función
# especimen_mas_inclinado(lista_arboles) que, dada una lista de árboles devuelva la
# especie que tiene el ejemplar más inclinado y su inclinación.
# Correlo para los tres parques mencionados anteriormente.
# Resultados. Deberías obtener, por ejemplo, que en el Parque Centenario hay un Falso Guayabo
# inclinado 80 grados.

def especimen_mas_inclinado(lista_arboles):
  arbolMasInclinado = lista_arboles[0]
  for tree in lista_arboles:
    if float(tree['inclinacio']) > float(arbolMasInclinado['inclinacio']):
      arbolMasInclinado = tree
  return arbolMasInclinado

print(' ')
for park in parks:
  arbolInclinado = especimen_mas_inclinado(leer_parque(
      '../Data/arbolado-en-espacios-verdes.csv', park))
  nombreArbolInclinado = arbolInclinado['nombre_com']
  gradosArbolInclinado = arbolInclinado['inclinacio']

  print(f'El arbol más inclinado del {park}\
  es un {nombreArbolInclinado} y tiene\
  {gradosArbolInclinado} grados')


# Ejercicio 2.28: Especie con más inclinada en promedio
# Volvé a combinar las funciones anteriores para escribir la función 
# especie_promedio_mas_inclinada(lista_arboles) que, dada una lista de árboles devuelva
# la especie que en promedio tiene la mayor inclinación y el promedio calculado..
# Resultados. Deberías obtener, por ejemplo, que los Álamos Plateados del Parque
#  Los Andes tiene un promedio de inclinación de 25 grados.
def especie_promedio_mas_inclinada(lista_arboles):
  speciesList = especies(lista_arboles)
  result = {
    'especie': '',
    'inclinacion_prom': 0.0
  }

  for specie in speciesList:
    angleList = obtener_inclinaciones(lista_arboles, specie)
    inclinacionPromedio = 0.0
    for angle in angleList:
      inclinacionPromedio += float(angle)
    inclinacionPromedio /= len(angleList)
    
    if float(inclinacionPromedio) > float(result['inclinacion_prom']):
      result['inclinacion_prom'] = float(inclinacionPromedio)
      result['especie'] = specie
  return result

print(' ')
for park in parks:
  especieMasInclinada = especie_promedio_mas_inclinada(leer_parque(
      '../Data/arbolado-en-espacios-verdes.csv', park))
  
  especie = especieMasInclinada['especie']
  inclinacionPromedio = especieMasInclinada['inclinacion_prom']

  print(f'La especie en promedio más inclinada en el parque\
  {park} es {especie} con una inclianción promedio de {inclinacionPromedio}')


# Preguntas extras: ¿Qué habría que cambiar para obtener la especie con un ejemplar
# más inclinado de toda la ciudad y no solo de un parque? ¿Podrías dar la latitud y longitud
# de ese ejemplar? ¿Y dónde se encuentra(lat, lon) el ejemplar más alto? ¿De qué especie es?
def encontrarArbolMasInclinado(filename):
  try:
    fileRaw = open(filename)
  except:
    return 'No se encuentra el archivo :('
  fileCsv = csv.reader(fileRaw)
  headers = next(fileCsv)
  arbolMasInclinado = dict(zip(headers, next(fileCsv)))
  for tree in fileCsv:
    accu = dict(zip(headers, tree))
    if float(accu['inclinacio']) > float(arbolMasInclinado['inclinacio']):
      arbolMasInclinado = accu
  return arbolMasInclinado


arbol = encontrarArbolMasInclinado('../Data/arbolado-en-espacios-verdes.csv')
print(f'El arbol más inclinado de la ciudad es:', arbol)

from pprint import pprint
import sys 
import csv

# leer_camion abre un archivo con el contenido de un camión, 
# lo lee y devuelve la información como una lista de tuplas
def leer_camion(filename):
  try: 
    csvRaw = open(filename)
  except: 
    return 'No encuentro el archivo :('
  csvData = csv.reader(csvRaw)
  truckLoad = []
  truckLoad.append(next(csvData))
  for csvSingleLineData in csvData:
    truckLoad.append(tuple(csvSingleLineData))
  return truckLoad


# a partir de un conjunto de precios como éste arme un diccionario donde las claves
# sean los nombres de frutas y verduras, y los valores sean los precios por cajón.
def leer_precios(filename):
  try:
    fileRaw = open(filename)
  except:
    return 'No se encuentra el archivo'
  fileData = csv.reader(fileRaw)
  dictionary = {}
  for fileDataSingle in fileData:
    try:
      dictionary[fileDataSingle[0]] = float(fileDataSingle[1])
    except:
      pass
  return dictionary


# completa el programa para que con los precios del camión (Ejercicio 2.13) y los de venta
# en el negocio (Ejercicio 2.14) calcule lo 
# que costó el camión, lo que se recaudo con la venta, y la diferencia. ¿Hubo 
# ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.

dataCostoCamion = leer_camion('../Data/camion.csv')

tablaDePrecios = leer_precios('../Data/precios.csv')
print('dataCostoCamion: ', dataCostoCamion)
print('tablaDePrecios: ', tablaDePrecios)

costoTotal = 0
headings = dataCostoCamion[0]
for cajones in dataCostoCamion:
  try:
    cajonesFormat = dict(zip(headings,cajones))
    costoTotal += int(cajonesFormat['cajones']) * float(cajonesFormat['precio'])
  except:
    pass

facturacionTotal = 0
for cajones in dataCostoCamion:
  try:
    cajonesFormat = dict(zip(headings, cajones))
    print(cajonesFormat)
    facturacionTotal += int(cajonesFormat['cajones']) * tablaDePrecios[cajonesFormat['nombre']]
  except: 
    pass
gananciaNeta = round(facturacionTotal - costoTotal,2)

print(f'En total se gasto {costoTotal} y se facturó\
  {facturacionTotal} dejando una ganancia neta de\
  {gananciaNeta}')

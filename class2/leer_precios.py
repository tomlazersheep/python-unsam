import csv 
from pprint import pprint

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


pprint(leer_precios('../Data/precios.csv'))

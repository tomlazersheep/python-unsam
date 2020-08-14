import csv 
import sys 

def truckCost(dataUrl):
  with open(dataUrl) as truckDataRaw:
    # uso csv module
    truckData = csv.reader(truckDataRaw)
    next(truckData)
    cost = 0
    for boxData in truckData:
      #para cada caja intento sacarle los datos
      try:
        cost += float(boxData[1]) * float(boxData[2])
      except ValueError:
        print('Hay una línea con datos ilegibles en el archivo! Ignorando...')
        continue 
    return cost 

if len(sys.argv) == 2:
  fileName = sys.argv[1]
  print(truckCost(fileName))
else:
  print('Missing arguments')
    
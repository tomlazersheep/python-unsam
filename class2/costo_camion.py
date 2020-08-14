'''
Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad
de cajones cargados en el camión, y un precio de compra por cada cajón de ese
grupo. Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas,
y calcule el precio pagado por los cajones cargados en el camión.
'''
import csv 

def costo_camion(dataUrl):
  with open(dataUrl) as truckDataRaw:
    # uso csv module
    truckData = csv.reader(truckDataRaw)
    cost = 0
    for boxData in truckData:
      #para cada caja intento sacarle los datos
      try:
        cost += float(boxData[1]) * float(boxData[2])
      except ValueError:
        print('Hay una línea con datos ilegibles en el archivo! Ignorando...')
        continue 
    return cost 


costo = costo_camion('../Data/missing.csv')

print(f'Costo Total en missing.csv: {costo}')

costo = costo_camion('../Data/camion.csv')

print(f'Costo Total en camion.csv: {costo}')

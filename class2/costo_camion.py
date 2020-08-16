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
    headings = next(truckData)
    cost = 0
    for i,boxData in enumerate(truckData, start=2):
      formatData = dict(zip(headings,boxData))
      #para cada caja intento sacarle los datos
      try:
        cost += int(formatData['cajones']) * float(formatData['precio'])
      except ValueError:
        print(f'Línea {i} con datos ilegibles en el archivo! Ignorando...{boxData}')
        continue 
    return cost 


costo = costo_camion('../Data/missing.csv')

print(f'Costo Total en missing.csv: {costo}')

costo = costo_camion('../Data/fecha_camion.csv')

print(f'Costo Total en fecha_camion.csv: {costo}')

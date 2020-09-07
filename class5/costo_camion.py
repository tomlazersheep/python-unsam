'''
Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad
de cajones cargados en el camión, y un precio de compra por cada cajón de ese
grupo. Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas,
y calcule el precio pagado por los cajones cargados en el camión.
'''
import csv 
import informe_funciones as informe

def costo_camion(dataUrl):
    truckData = informe.leer_camion(dataUrl)
    print("truckData  ", truckData )
    cost = 0
    
    for boxData in truckData:

      #para cada caja intento sacarle los datos
      try:
        cost += int(boxData[-2]) * float(boxData[-1])
      except ValueError:
        print(f'Línea con datos ilegibles en el archivo! Ignorando...{boxData}')
        continue 
    return cost 


costo = costo_camion('../Data/missing.csv')

print(f'Costo Total en missing.csv: {costo}')

costo = costo_camion('../Data/fecha_camion.csv')

print(f'Costo Total en fecha_camion.csv: {costo}')

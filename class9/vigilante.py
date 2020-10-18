# vigilante.py
import os
import time
import informe

def vigilar(filename):
  f = open(filename)
  f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF

  while True:
    line = f.readline()
    if line == '':
      continue          # vuelve al comienzo del while
    fields = line.split(',')
    volumen = int(fields[2])
    if volumen >= 1000:
      yield line

if __name__ == '__main__':
  
  camion = informe.leer_camion ('../Data/camion.csv')
    
  for line in vigilar('../Data/mercadolog.csv'):
    fields = line.split(',')
    nombre = fields[0].strip('"')
    precio = float(fields[1])
    volumen = int(fields[2])
    
    if nombre in camion:    
      print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')

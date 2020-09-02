# Ejercicio 4.8: Envido
# Teniendo en cuenta las reglas del Truco, estimá la probabilidad de 
# obtener 31, 32 o 33 puntos de envido en una mano. ¿Son iguales estas tres 
# probabilidades? ¿Por qué?

# Si se poseen dos o más cartas de igual palo, el tanto equivale a la
# suma del puntaje de dos cartas del mismo palo elegidas por el jugador
# más veinte puntos(10, 11 y 12 no suman)

import random
from collections import Counter

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

def calcular_puntos():
  mano = random.sample(naipes, k=3)
  puntos = 20
  palos_mano = []

  for carta in mano:
    palos_mano.append(carta[1])

  envido = Counter(palos_mano).most_common()[0]
  
  if envido[1] > 1:
    for carta in mano:
      if (envido[0] == carta[1]) and (carta[0] < 8):
        puntos += carta[0]
    return puntos
  else: 
    return 0

manos = 10000000
p31 = 0
p32 = 0
p33 = 0

for _ in range(manos):
  puntos = calcular_puntos()
  if puntos == 31:
    p31 += 1
  elif puntos == 32:
    p32 += 1
  elif puntos == 33: 
    p33 += 1

print(f'Se repartieron {manos} manos:')
print(f'{p31} veces salio el puntaje 31, probabilidad: {(p31/manos):<10f}') #0.028296
print(f'{p32} veces salio el puntaje 32, probabilidad: {(p32/manos):<10f}') #0.015348
print(f'{p33} veces salio el puntaje 33, probabilidad: {(p33/manos):<10f}') #0.014934


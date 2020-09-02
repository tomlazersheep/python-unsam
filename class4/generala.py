
# Ejercicio 4.7: Generala no necesariamente servida
# Si uno juega con las reglas originales(se puede volver a tirar algunos
#  de los cinco dados hasta dos veces, llegando hasta a tres tiradas en total)
#  siguiendo una estrategia que intente obtener generala(siempre guardar los
#  dados que más se repiten y tirar nuevamente los demás) es más probable otener
#  una generala que si sólo consideramos la generala servida. Escribí un programa
#  que estime la probabilidad de obtener una generala en las tres tiradas de una mano
#  y guardalo en un archivo generala.py.

import random
from collections import Counter

def throw_dice(dices):                 # funcion que devuelve una tirada de n dados en forma de lista
  results = []
  for _ in range(dices):
    results.append(random.randint(1,6))
  return results

def is_generala(dice_values):          # funcion para determinar si un juego de resultados es generala
  return len(set(dice_values)) == 1

def play_generala():                   # jugar un juego de generala con 3 tiradas
  resultados = []                      # acá guardo los valores de dados de cada juego
  target = None                        # esta variable será el valor al que apunto tener 5 repeticiones
  dados_a_tirar = 5                    # arranco tirando los 5 dados
  for _ in range(3):
    resultados.extend(throw_dice(dados_a_tirar))  #agrego los resultados de tirar los dados
    if is_generala(resultados):                   #si saqué generala devuelvo True y salgo
      return True
    target = Counter(resultados).most_common()[0] #de lo contrario cuento cuál es el número más común
    resultados = [target[0]] * target[1]          #en mis resultados ya dejo las instancias de ese numero
    dados_a_tirar = 5 - target[1]                 # vuelvo a tirar la cantidad de dados que no tengan mi número objetivo
  return False                                    # si después de las 3 tiradas no logro generala, devuelvo False


#Estimar probabilidad de obtener generala 

jugadas = 1000000
victorias = 0

for _ in range(jugadas):
  if play_generala():
    victorias += 1

print(f'Se jugó a la generala {jugadas} veces y se obtuvo la generala en {victorias} ocasiones:')
print(f'probabilidad: {victorias/jugadas:<.6f}') #aparentemente alrededor de 0,046 
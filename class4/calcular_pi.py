# Si el área del círculo completo es pi, el área de nuestro cuarto de
# círculo es pi/4. Por otro lado el área del cuadrado unitario es 1.
# Por lo tanto, si generamos N puntos con una distribución uniforme en el 
# cuadrado unitario, esperamos que pi/4 de estos N puntos caigan dentro del cuarto
# del círculo y el resto afuera. Es decir que, si llamamos M al número de puntos
# que caen dentro del círculo, esperamos que M ~(pi/4 * N).

# Despejando pi de esta estimación, obtenemos que pi ~ 4*M/N. Esto nos permite estimar
# pi mirando cuántos puntos caen realmente dentro del círculo del total de puntos.

# Ejercicio 4.10: Estimar pi
# Escribí un programa estimar_pi.py que genere cien mil puntos aleatorios con la
# función generar_punto(), calcule la proporción de estos puntos que caen en el
# círculo unitario(usando ¿x ^ 2 + y ^ 2 < 1?) y use este resultado para
# dar una aproximación de pi.

import random

def generar_punto():
  return (random.random(), random.random())

N = 9000000
M = 0

for _ in range(N):
  punto = generar_punto()
  if ((punto[0]**2) + (punto[1]**2)) < 1:
    M += 1

print(f'La aproximación de pi con N = {N} y M = {M} es: {(4*(M/N)):<5f}')
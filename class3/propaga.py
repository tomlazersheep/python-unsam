# Ejercicio 3.9: Propagación
# Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden
#  estar en tres estados: nuevos, prendidos fuego o ya gastados(carbonizados). Representaremos esta situación con
#  una lista L con un elemento por fósforo, que en cada posición tiene un 0 (nuevo), un 1 (encendido)
#  o un - 1 (carbonizado). El fuego se propaga inmediatamente de un fósforo encendido a cualquier fósoforo nuevo 
# que tenga a su lado. Los fósforos carbonizados no se encienden nuevamente.

# Escribí una función llamada propagar que reciba un vector con 0's, 1's y - 1's y devuelva un
# vector en el que los 1's se propagaron a sus vecinos con 0. Guardalo en un archivo propaga.py.

# Por ejemplo:

# >> > propagar([0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0])
# [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
# >> > propagar([0, 0, 0, 1, 0, 0])
# [1, 1, 1, 1, 1, 1]

# 1 ENCENDIDO -> propaga
# 0 NUEVO -> puede encenderse
# -1 CARBONIZADO -> no se enciende ni propaga


def propagar(data):
  fire = data
  for _ in range(len(data)-1):        # worst case scenario: n-1 cycles for full propagation
    for i,match in enumerate(fire):
      if match == 1:                  #if matchhead has fire
        
        if (i > 0):                   # check if it's the first match
          if (fire[i-1] == 0):        # if there is a previus match, check for head state
            fire[i-1] = 1             # propagate fire if previous matchead is 0

        if (i < len(data)-1):         # check for last match
          if (fire[i+1] == 0):        # if not last match, check next match status
            fire[i+1] = 1             # propagate fire if next matchead is 0

  return fire


args = [[0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]]

print('propagar')
for arg in args:
  print(f'{arg} --> {propagar(arg)}')
print('')


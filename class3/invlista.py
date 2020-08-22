# Ejercicio 3.8: Invertir una lista
# Escribí una función invertir_lista(lista) que dada una lista devuelva otra que tenga los
# mismos elementos pero en el orden inverso. Es decir, el que era el primer elemento de la lista de
# entrada deberá ser el último de la lista de salida y análogamente con los demás elementos.
def invertir_lista(lista):
  invertida = []
  for e in lista:  # Recorro la lista
    invertida.insert(0,e)
  return invertida


args = [[1, 2, 3, 4, 5], ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']]

for arg in args:
  print('invertir_lista')
  for arg in args:
    print(f'{arg} --> {invertir_lista(arg)}')
  print('')

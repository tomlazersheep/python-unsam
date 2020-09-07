# Modificando la función busqueda_binaria(lista, x) adecuadamente,
# definí una función donde_insertar(lista, x) de forma que reciba una
# lista ordenada y un elemento y devuelva la posición de ese elemento
# en la lista(si se encuentra en la lista) o la posición donde se podría
# insertar el elemento para que la lista permanezca ordenada
# (si no está en la lista).

# Por ejemplo: el elemento 3 podría insertarse en la posición 2 en la 
# lista[0, 2, 4, 6] para mantenerla ordenada. Por lo tanto, el llamado 
# donde_insertar([0, 2, 4, 6], 3) deberá devolver 2, al igual que el 
# llamado donde_insertar([0, 2, 4, 6], 4).

def donde_insertar(lista, x):
  '''recibe una lista ordenada y un elemento y devuelve la posición de ese elemento
  en la lista(si se encuentra en la lista) o la posición donde se podría
  insertar el elemento para que la lista permanezca ordenada
  (si no está en la lista).'''
  pos = None  # Inicializo respuesta, el valor no fue encontrado
  izq = 0
  der = len(lista) - 1
  comps = 0
  while izq <= der:
    comps +=1
    medio = (izq + der) // 2
    comps += 1
    if lista[medio] == x:
      pos = medio     # elemento encontrado!
    comps += 1
    if lista[medio] > x:
      der = medio - 1  # descarto mitad derecha
    else:               # if lista[medio] < x:
      izq = medio + 1  # descarto mitad izquierda
  comps += 1
  if pos == None:
    return izq,comps
  return pos,comps



# Usando lo que hiciste en el Ejercicio 5.11, agregale al archivo bbin.py una 
# función insertar(l, e) que reciba una lista ordenada l y un elemento y e. 
# Si el elemento se encuentra en la lista solamente devuelve su posición
# si no se encuentra en la lista, lo inserta en la posición correcta para 
# mantener el orden. En este segundo caso, también debe devolver su posición.

def insertar(l,e):
  pos,comps = donde_insertar(l,e)
  if l[pos] == e:
    pass
  else: 
    l.insert(pos, e)
  return l,pos,comps


print("insertar([0, 2, 4, 6], 4)--->", insertar([0, 2, 4, 6], 4))
print('')
print("insertar([0, 2, 4, 6], 3)--->", insertar([0, 2, 4, 6], 3))

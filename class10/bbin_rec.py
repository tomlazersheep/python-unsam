# Ejercicio 10.11: Búsqueda binaria
# Escribí una función recursiva que implemente la búsqueda binaria de un elemento e 
# en una lista ordenada lista. La función debe devolver simplemente True o False 
# indicando si el elemento está o no en a lista. Para esto completá el siguiente código:

def bbinaria_rec(lista, e):
  if len(lista) == 0:
    res = False
  elif len(lista) == 1:
    res = lista[0] == e
  else:
    medio = len(lista)//2
    if lista[medio] == e:
      res = True
    elif lista[medio] > e:
      return bbinaria_rec(lista[:medio],e)
    elif lista[medio] < e:
      return bbinaria_rec(lista[medio:],e)

  return res

# >>> bbinaria_rec([1,2,3,4,5,6,7,8,9],4)
# True
# >>> bbinaria_rec([1,2,3,4,5,6,7,8,9],90)
# False
# >>> bbinaria_rec([1,2,3,4,5,6,7,8,9],1)
# True
# >>> bbinaria_rec([1,2,3,4,5,6,7,8,9],2)
# True
# >>> bbinaria_rec([1,2,3,4,5,6,7,8,9],3)
# True
# >>> bbinaria_rec([1,2,3,4,5,6,7,8,9],8)
# True
# >>> bbinaria_rec([1,2,3,4,5,6,7,8,9],7)
# True
# >>> bbinaria_rec([1,2,3,4,5,6,7,8,9,900],70)
# False
# >>> 


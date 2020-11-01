def merge_sort(lista):
  if len(lista) <= 1:
    return lista
  else:
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)

def merge(izq,der):
  return True


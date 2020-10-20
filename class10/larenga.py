# Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k

def pascal(n, k):
  if n == k or k == 0:
    return 1
  else:
    return pascal(n-1,k-1) + pascal(n-1,k)

print(pascal(5,2))
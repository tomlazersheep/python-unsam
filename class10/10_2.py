# Ejercicio 10.2: Números triangulares
# Escribí una función que calcule recursivamente el n-ésimo número triangular 
# (es decir, el número 1 + 2 + 3 + ... + n).

def enesimo_triangular(n):
  if n == 1:
    return 1
  else: 
    return n + enesimo_triangular(n-1)


# Ejercicio 10.3: Dígitos
# Escribí una función recursiva que reciba un número positivo, n, y devuelva la cantidad de dígitos que tiene.

def nro_digitos(n):
  if n < 10:
    return 1
  else:
    return 1 + nro_digitos(n/10)


# Ejercicio 10.4: Potencias
# Escribí una función recursiva que reciba 2 enteros, n y b, y devuelva True si n es potencia de b.

def is_pot(n,b):
  if b > n:
    return False
  elif n == b:
    return True
  else:
    return is_pot(n, b*b) 
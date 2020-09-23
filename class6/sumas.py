def sumar_enteros_ciclo(desde, hasta):
  '''Calcula la sumatoria de los números entre desde y hasta.
    Si hasta < desde, entonces devuelve cero.

  Pre: desde y hasta son números enteros
  Pos: Se devuelve el valor de sumar todos los números del intervalo
    [desde, hasta]. Si el intervalo es vacío se devuelve 0
  '''
  if (type(desde) != int) or (type(hasta) != int):
    raise RuntimeError('Los parametros deben ser enteros')
  
  if hasta < desde:
    return 0
  
  suma = 0
  for i in range(desde,hasta+1):
    suma += i
  
  return suma

def sumar_enteros_sin_ciclo(desde, hasta):
  '''Calcula la sumatoria de los números entre desde y hasta.
    Si hasta < desde, entonces devuelve cero.

  Pre: desde y hasta son números enteros
  Pos: Se devuelve el valor de sumar todos los números del intervalo
    [desde, hasta]. Si el intervalo es vacío se devuelve 0
  '''
  if (type(desde) != int) or (type(hasta) != int):
    raise RuntimeError('Los parametros deben ser enteros')
  if hasta < desde:
    return 0
  
  suma_desde = (desde * (desde+1) * (desde+2))/6
  suma_hasta = (hasta * (hasta+1) * (hasta+2))/6
  return suma_desde,suma_hasta
# Ejercicio 8.12: Torre de Control
# Usando un par de objetos de la clase Cola, escribí una nueva clase llamada 
# TorreDeControl que modele el trabajo de una torre de control de un 
# aeropuerto con una pista de aterrizaje. Los aviones que están esperando para aterrizar tienen 
# prioridad sobre los que están esperando para despegar. 

class Cola:
  '''
  Crea una lista y provee metodos de cola
  '''
  def __init__(self):
    self.cola = []
  
  def encolar(self, item):
    '''
    agrega un item al final de la cola
    '''
    self.cola.append(item)
  
  def desencolar(self):
    '''
    saca el primer elemento de la cola y lo retorna
    '''
    return self.cola.pop(0)

  def esta_vacia(self):
    '''
    retorna true si la cola está vacía
    '''
    return True if len(self.cola) == 0 else False

class TorreDeControl:
  def __init__(self):
    self.arriving = Cola()
    self.departing = Cola()
  
  def nuevo_arribo(self, arrive):
    self.arriving.encolar(arrive)
  
  def nueva_partida(self, departure):
    self.departing.encolar(departure)
  
  def ver_estado(self):
    print(f'Vuelos esperando para aterrizar: {*self.arriving.cola,}')
    print(f'Vuelos esperando para despegar: {*self.departing.cola,}')

  def asignar_pista(self):
    if self.arriving.esta_vacia():
      if self.departing.esta_vacia():
        print('No hay vuelos pendientes')
      else:
        print(f'El vuelo {self.departing.desencolar()} despegó con exito.')
    else:
      print(f'El vuelo {self.arriving.desencolar()} aterrizó con exito.')


torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
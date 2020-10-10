class Punto():
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def add(self, otro_punto):
    self.x += otro_punto.x
    self.y += otro_punto.y

  def __str__(self):
    return f'({self.x}, {self.y})'

  # Used with `repr()`
  def __repr__(self):
    return f'Punto({self.x}, {self.y})'

class Rectangulo:
  def __init__(self,punto1,punto2):
    '''
    Constructor. Crea un rectángulo a partir de 2 puntos.
    '''
    if punto1.x == punto2.x or punto1.y == punto2.y:
      raise RuntimeError('It is a line')

    self.punto_izq_up = Punto(punto1.x if punto1.x < punto2.x else punto2.x,
                              punto1.y if punto1.y > punto2.y else punto2.y)

    self.punto_der_be = Punto(punto1.x if punto1.x > punto2.x else punto2.x,
                              punto1.y if punto1.y < punto2.y else punto2.y)

  def base(self):
    '''
    que dé la medida de la base del rectángulo.
    '''
    return self.punto_der_be.x - self.punto_izq_up.x
  
  def altura(self):
    '''
    que dé la medida de la altura del rectángulo.
    '''
    return self.punto_izq_up.y - self.punto_der_be.y
  
  def area(self):
    '''
    Da el area del rectangulo
    '''
    return self.altura() * self.base()

  def __str__(self):
    return f'({self.punto_izq_up.x},{self.punto_izq_up.y})------------\n\n\n-------------({self.punto_der_be.x},{self.punto_der_be.y})'

  def __repr__(self):
    print(self.punto_izq_up)
    print(self.punto_der_be)
    return ''
  
  def desplazar(self,desplazamiento):
    '''
    desplaza el rectángulo tomando un punto como vector de desplazamiento
    '''
    self.punto_der_be.add(desplazamiento)
    self.punto_izq_up.add(desplazamiento)

  def rotar(self):
    h = self.altura()
    b = self.base()
    self.punto_der_be.add(Punto(h,0))
    self.punto_izq_up = Punto(self.punto_izq_up.x + b, self.punto_der_be.y + b)

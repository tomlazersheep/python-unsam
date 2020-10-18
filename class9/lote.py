class Lote():
  def __init__(self, nombre, cajones, precio):
    self.nombre = nombre
    self.cajones = cajones
    self.precio = precio
  
  def costo(self):
    return self.cajones * self.precio

  def vender(self, vendidos):
    self.cajones -= vendidos
  
  def __repr__(self):
    return f'\nnombre: {self.nombre}\ncajones: {self.cajones}\nprecio: {self.precio}\n'


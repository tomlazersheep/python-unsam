# Ejercicio 10.14: precio_alquiler ~ superficie
# Consideramos datos de precios (en miles de pesos) de alquiler mensual de departamentos en el barrio de Caballito,
# CABA, y sus superficies (en metros cuadrados). Queremos modelar el precio de alquiler a partir de la
# superficie para este barrio. A veces este modelo se nota con precio_alquiler ~ superficie.

# Usando la función que definimos antes, ajustá los datos con una recta.
# Graficá los datos junto con la recta del ajuste.
# superficie = np.array([150.0, 120.0, 170.0, 80.0])
# alquiler = np.array([35.0, 29.6, 37.4, 21.0])

import numpy as np
from matplotlib import pyplot as plt

def ajuste_lineal_simple(x,y):
  a = sum(((x - x.mean())*(y - y.mean()))) / sum(((x - x.mean())**2))
  b = y.mean() - a*x.mean()
  return a,b

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a,b = ajuste_lineal_simple(superficie,alquiler)
grilla_x = np.linspace(50,200,50)
grilla_y = grilla_x*a + b

g = plt.scatter(x=superficie, y=alquiler)
plt.plot(grilla_x,grilla_y,c='green')
plt.scatter(x=superficie, y=alquiler)
plt.title('alquiler vs superficie')
plt.xlabel('superficie')
plt.ylabel('alquiler')
plt.show()


# Una forma de cuantificar cuán bien ajusta la recta es considerar el promedio de
#  los errores cuadráticos, llamado error cuadrático medio.

errores = alquiler-(a*superficie + b) # valor real de alquiler menos lo que arroja la aproximación lineal
print("Error Cuadratico Medio:", (errores**2).mean()) 


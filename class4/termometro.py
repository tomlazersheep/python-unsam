# Hagamos algún ejercicio sencillo antes de terminar. Supongamos que una persona 
# se compra un termómetro que mide la temperatura con un error aleatorio normal con 
# media 0 y desvío estándar de 0.2 grados(error gaussiano). Si la temperatura 
# real de la persona es de 37.5 grados, simulá usando normalvariate()(con mu y sigma 
# adecuados) n = 99 valores medidos por el termómetro.

# Imprimí los valores obtenidos en las mediciones de temperatura simuladas y luego, 
# como resumen, cuatro líneas indicando el valor máximo, el mínimo, el promedio y la 
# mediana de estas n mediciones. Guardá tu programa en el archivo termometro.py.

import random
import numpy as np

mu = 37.5
varianza = 0.2
sigma = varianza**0.5
n = 999

valores = []

for _ in range(n):
  valores.append(random.normalvariate(mu,sigma))

print(valores)
print(f'Valor máximo: {max(valores)}')
print(f'Valor minimo: {min(valores)}')
print(f'Valor promedio: {sum(valores)/n}')
valores.sort()
print(f'Valor mediana: {valores[49]}')

# Ejercicio 4.13: Guardar temperaturas
# Ampliá el código de termometro.py que escribiste en el Ejercicio 4.11 para
# que guarde el vector con las temperaturas simuladas en el directorio Data
# de tu carpeta de ejercicios, en un archivo llamado Temperaturas.npy. Hacé
# que corra 999 veces en lugar de solo 99.

np.save('../Data/Temperaturas', np.array(valores))
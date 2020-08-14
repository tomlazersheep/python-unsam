# rebotes.py
# Archivo de ejemplo
# Ejercicio
height = 100
iterations = input ('how many bounces?')

for x in range(int(iterations)):
    height *= (3/5)
    print(round(height,4))


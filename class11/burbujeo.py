# Programá una función ord_burbujeo(lista) que implemente este método 
# de ordenamiento. ¿Cuántas comparaciones realiza esta función en una lista de largo n?

lista_1 = [1, 2, -3, 8, 1, 5]
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
lista_4 = [10, 8, 6, 2, -2, -5]
lista_5 = [2, 5, 1, 0]
# Agrego otra lista de más elementos para hacer más evidente la complejidad
lista_6 = [3,234,3,45,21,-123,34-1233,0,90,34,-4,-9,123123,123,123,4,3,5,6,4,3,5,6]

def ord_burbujeo(lista):
  lista_copy = lista.copy()
  steps = 0
  for _ in lista_copy:
    for j,_ in enumerate(lista_copy[:-1]):
      steps += 1
      if lista_copy[j] > lista_copy[j+1]:
        aux = lista_copy[j]
        lista_copy[j] = lista_copy[j+1]
        lista_copy[j+1] = aux
  return lista_copy,steps

listas = [lista_1, lista_2, lista_3, lista_4, lista_5, lista_6]

resultados = [ ord_burbujeo(lista_n) for lista_n in listas ]

print(resultados)

# analizar complejidad según largo de la lista
import pandas as pd
import matplotlib.pyplot as plt

x_axis = [len(lista_n[0]) for lista_n in resultados]

y_axis = [lista_n[1] for lista_n in resultados]
data = pd.DataFrame({'lenghts':x_axis,'steps':y_axis})
data.plot(x='lenghts',y='steps',kind='scatter')
plt.show() #En el gráfico se ve que se comporta de forma cuadrática
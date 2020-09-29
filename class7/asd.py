# Levantalo y armá un DataFrame df_lineal que tenga solamente las siguiente columnas:

# cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
# Imprimí las diez especies más frecuentes con sus respectivas cantidades.

# Trabajaremos con las siguientes especies seleccionadas:
# especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

# Una forma de seleccionarlas es la siguiente:

# df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

import pandas as pd 
import matplotlib
import seaborn as sbn

df_lineal = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')

df_most_frequent_type = df_lineal['nombre_cientifico'].value_counts()

print(df_most_frequent_type.head(10))

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_especies = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

# df_especies.boxplot('diametro_altura_pecho', by='nombre_cientifico')
# df_especies.boxplot('altura_arbol', by='nombre_cientifico')

sbn.pairplot(data=df_especies, hue='nombre_cientifico')

matplotlib.pyplot.show()
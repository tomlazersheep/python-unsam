# Ejercicio 7.9: Comparando especies en parques y en veredas

# Abrí ambos datasets a los que llamaremos df_parques y df_veredas.
# Para cada dataset armate otro seleccionando solamente las filas correspondientes a las tipas 
# (llamalos df_tipas_parques y df_tipas_veredas, respectivamente) y las columnas 
# correspondientes al diametro a la altura del pecho y alturas. 
# Hacelo como copias (usando .copy() como hicimos más arriba) para poder trabajar en estos nuevos 
# dataframes sin modificar los dataframes grandes originales. Renombrá las columnas que muestran la 
# altura y el diámetro a la altura del pecho para que se llamen igual en ambos dataframes, para ello explorá
# el comando rename.
# Agregale a cada dataframe (df_tipas_parques y df_tipas_veredas) una columna llamada 'ambiente' 
# que en un caso valga siempre 'parque' y en el otro caso 'vereda'.
# Juntá ambos datasets con el comando df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques]). 
# De esta forma tenemos en un mismo dataframe la información de las tipas distinguidas por ambiente.
# Creá un boxplot para los diámetros a la altura del pecho de la tipas distinguiendo los ambientes 
# (boxplot('diametro_altura_pecho',by = 'ambiente')).
# Repetí para alturas.
# ¿Qué tendrías que cambiar para repetir el análisis para otras especies? ¿Convendría definir una función?

import pandas as pd
import matplotlib 

PARQUES_PATH = '../Data/arbolado-en-espacios-verdes.csv'
VEREDAS_PATH = '../Data/arbolado-publico-lineal-2017-2018.csv'

df_parques = pd.read_csv(PARQUES_PATH)
df_veredas = pd.read_csv(VEREDAS_PATH)

df_tipas_parques = df_parques[df_parques.nombre_cie.eq('Tipuana Tipu')].copy()
df_tipas_veredas = df_veredas[df_veredas.nombre_cientifico.eq('Tipuana tipu')].copy()

df_tipas_parques.rename(columns={"diametro": "diametro_altura_pecho"}, inplace=True)
df_tipas_parques.rename(columns={"altura_tot": "altura_arbol"}, inplace=True)

df_tipas_parques['ambiente'] = "parque"
df_tipas_veredas['ambiente'] = "vereda"

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

df_tipas.boxplot('diametro_altura_pecho', by="ambiente")
df_tipas.boxplot('altura_arbol', by="ambiente")



matplotlib.pyplot.show()

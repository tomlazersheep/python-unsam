# Ejercicio 11.10: Seaborn
# Repetí el gráfico anterior pero usando seaborn en lugar de 
# pandas para graficar

# Sugerencia: Usando iris_dataframe['target'] = iris_dataset['target'], agregá al DataFrame 
# el atributo target de cada flor para poder 
# hacer un sns.pairplot() seteando hue sobre las especies de iris.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import sklearn.datasets


iris_dataset = sklearn.datasets.load_iris()



iris_dataframe = pd.DataFrame(iris_dataset['data'], columns=iris_dataset['feature_names'])

iris_dataframe['target'] = iris_dataset['target']

# otra forma:
# iris_dataframe.insert(len(iris_dataframe.columns),'target', iris_dataset['target'])

print(iris_dataframe)

sbn.pairplot(iris_dataframe,
             hue='target',
             palette={1:'green',0:'red',2:'blue'})
plt.show()
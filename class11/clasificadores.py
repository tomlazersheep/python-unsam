import pandas as pd
import matplotlib.pyplot as plt

import sklearn.datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


iris_dataset = sklearn.datasets.load_iris()

# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names

x_train, x_test, y_train, y_test = tts(iris_dataset['data'], iris_dataset['target'], random_state=0)

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(x_train,y_train)

x_new = np.array([5, 2.9, 1, 0.2]).reshape(1,-1)

prediction = knn.predict(x_new)
print(f'Predicción para {x_new}: {iris_dataset["target_names"][prediction]}')

print(f'Score del modelo K-Nearest Neighbors: {knn.score(x_test, y_test)}')

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

x_train, x_test, y_train, y_test = tts(iris_dataset['data'], 
                                       iris_dataset['target'])

clf.fit(x_train,y_train)

print()
print(f'Score del modelo Tree: {clf.score(x_test, y_test)}')

print()
print ('# Repetir 100 veces cada modelo y comparar scores')
N = 100

score_sum_knn = 0
score_sum_clf = 0

for _ in range(N):
  x_train, x_test, y_train, y_test = tts(iris_dataset['data'], 
                                       iris_dataset['target'])
  knn.fit(x_train, y_train)
  score_sum_knn += knn.score(x_test,y_test)
  
  clf.fit(x_train, y_train)
  score_sum_clf += clf.score(x_test,y_test)

print(f'score_sum_knn: {score_sum_knn/N}') #este me suele dar mejor
print(f'score_sum_clf: {score_sum_clf/N}')
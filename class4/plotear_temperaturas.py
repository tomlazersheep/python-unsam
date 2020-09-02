import numpy as np
import matplotlib.pyplot as plt 

data = np.load('../Data/Temperaturas.npy')


plt.hist(data,bins=40)
plt.show()
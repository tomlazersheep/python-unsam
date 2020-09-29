import pandas as pd
import matplotlib

dh = pd.read_csv('../Data/mareas.csv', index_col=['Time'], parse_dates=True)

    
delta_t = 0 # tiempo que tarda la marea entre ambos puertos
delta_h = 18 # diferencia de los ceros de escala entre ambos puertos
df = pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T
df['12-25-2014':].plot()
matplotlib.pyplot.show()
import pandas as pd, numpy as np

from numpy import NaN, NaN, nan


ebola = pd.read_csv('country_timeseries.csv')


# Cuente el número de valores que no faltan

print(ebola.count())

print()

num_rows = ebola.shape[0]

num_missing = num_rows - ebola.count()

print(num_missing)

print()

print(np.count_nonzero(ebola.isnull()))

print()

print(np.count_nonzero(ebola['Cases_Guinea'].isnull()))

print()

# Obteniendo los primeros 5 recuentos de valores de la columna Cases_Guinea

print(ebola.Cases_Guinea.value_counts(dropna=False).head())

print()

print(ebola.fillna(0).iloc[0:10, 0:5])

# Rellenar adelante

print()

print(ebola.fillna(method='ffill').iloc[0:10, 0:5])

print()


# Rellenar al revés

print(ebola.fillna(method='bfill').iloc[:,0:5].tail())

print()

# Interpolar

print()

print (ebola.interpolate().iloc[0:10, 0:5])

ebola_dropna = ebola.dropna()

print(ebola_dropna.shape)

print()

print(ebola_dropna)

print()


### Cálculo con datos faltantes

ebola['Cases_multiple'] = ebola['Cases_Guinea'] + \
                          ebola['Cases_Liberia'] + \
                          ebola['Cases_SierraLeone']    


print()


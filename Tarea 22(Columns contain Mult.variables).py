import pandas as pd


pew = pd.read_csv('pew.csv')

# Mostrar solo las primeras columnas

print(pew.iloc[:, 0:6])

print()


# No necesitamos especificar un value_vars ya que queremos pivotar
# Todas las columnas excepto la columna 'religión'

pew_long = pd.melt(pew, id_vars='religion')

print(pew_long.head()) # Imprimir los primeros 5

print()

print(pew_long.tail()) # Imprimir los ultimos 5



## Mantener múltiples columnas fijas

billboard = pd.read_csv('billboard.csv')

# Mira las primeras filas y columnas
print(billboard.iloc[0:5, 0:16])

print()

billboard_long = pd.melt(
    billboard, 
    id_vars=['year', 'artist', 'track', 'time', 'date.entered'], 
    var_name='week',
    value_name='rating')

print(billboard_long.head())

print(billboard_long.tail())

## Las columnas contienen múltiples variables

ebola = pd.read_csv('country_timeseries.csv')
print(ebola.columns)

print()

# Imprimir filas seleccionadas

print(ebola.iloc[:5, [0, 1 , 2 , 3 , 10 , 11]])

print()

ebola_long = pd.melt(ebola, id_vars=['Date', 'Day'])
print(ebola_long.head()) # Imprimir los 5 primeros

print()

print(ebola_long.tail()) # Imprimir los 5 ultimos 

## Dividir y agregar columnas individualmente (método simple)

# obtener la columna variable
# Accede a los métodos de cadena
# Y divide la columna según un delimitador

print()

variable_split = ebola_long.variable.str.split('_')
print(variable_split)
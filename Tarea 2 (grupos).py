import pandas as pd, matplotlib.pyplot as plt, numpy as np #Importamos la libreria

 
kombat = pd.read_csv('kombat1.csv')


print ('*******************************************')

### Desplegando medio de grupos 

grouped_kombat = kombat.groupby('Defensa') # Introducimos la funcion en una nueva variable

print(kombat.groupby('Defensa')['Ataque'].mean()) # obtenemos la columna 'Ataque' y calculamos la media

print ()

print('********************************************')

print(type(grouped_kombat))

print(grouped_kombat)

media_grupo = grouped_kombat.mean() 

print(media_grupo)

print('********************************************')

flat = media_grupo.reset_index() # Declaramos flat para aplanar marco de datos 
print(flat.head(15))

print('********************************************')


print()

### Frecuencia de conteo agrupada

# Usar el nunique (unico numero)

print(kombat.groupby('Defensa')['Ataque'].nunique())

### Trama Basica (Basic Plot)

var_g = kombat.groupby('Ataque')['Defensa'].mean()

print(var_g)

var_g.plot()

plt.show()

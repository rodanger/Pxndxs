# Importamos la libreria pandas 

import pandas as pd

# Declaramos la variable indicandole que vea el archivo
print("***************************")
kombat= pd.read_csv('kombat1.csv')

# Imprimimos el archivo
print (kombat.head(29))
print()

#Con esto podemos visualizar los nombres de las columnas Del Dataframe
print("***************************")
print(kombat.columns)

# Unicamente queremos ver las armas de los primeros 13 personajes
print("***************************")
host = pd.unique (kombat['Armas'].head(14))
print()
print(host)

# A continuacion veremos el nivel de resistencia desde el menos resistente al mas resistente
print("***************************")
dif= kombat['Defensa'].describe()
print()
print(dif)
print()
# Obteniendo todas la informacion de un personaje
print("***************************")
print(kombat.loc[2])

# Ahora vamos a acceder unicamente a 3 columnas del dataframe
print("***************************")
solo_3 = kombat[['Nombre ','Pais', 'Sexo']]
print(solo_3.head(30))
print("***************************")

#Tipo de valor de cada columna

tipo= kombat.dtypes
print(tipo)
print("***************************")
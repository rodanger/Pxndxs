# Importamos la libreria pandas 

import pandas as pd

# Declaramos la variable que nos permitira visualizar el archivo


kombat= pd.read_csv('kombat1.csv')

# Imprimimos el archivo
print(kombat.head(24))

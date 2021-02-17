import pandas as pd, numpy as np
 
from collections import OrderedDict

# Creando nuestra data

print ('*********************************************************************************') 

c = pd.Series (['Joe lopez', 'DevOp'], index = ['Persona', 'Who']) # Declaramos la variable que contendra las series

print (c) 

print ('*********************************************************************************')

# Creando un DataFrame

cientificos = pd.DataFrame( 
    data = {'Ocupacion': ['Ing. Quimico' , 'Astronomo', 'Bioquimicos' , 'Biofisico'] ,
     'Nacimiento': ['1971-08-23' , '1983-03-13' , '1975-04-11' , '1988-04-27'] ,
     'Muerte': ['2014-02-23' , '2019-05-24' , '2010-08-29' , '2017-10-17'] ,
      'Edad' : [43, 36, 35, 29 ]} ,
       index =  ['Andrea Castro' , 'Carlos de la rosa' , 'Jose Matos' , 'Carla Martinez' ] ,
     columns = ['Ocupacion' , 'Nacimiento' , 'Muerte' , 'Edad'])

print (cientificos) 

print ('*********************************************************************************')

#Seleccionar por etiqueta de índice de fila

primera_fila = cientificos.loc ['Carlos de la rosa']

print (type(primera_fila))

print (primera_fila)

print ('*********************************************************************************')     

Ages = cientificos['Edad']

print(Ages)

print ('*********************************************************************************') 

# Obtener estadísticas básicas

print(Ages.describe())

# Media en todas las edades

print (Ages.mean())

print ('*********************************************************************************') 
print (Ages[Ages>Ages.mean()])

print ()

print (Ages > Ages.mean())

print ()

print (type(Ages > Ages.mean()))

print ('*********************************************************************************') 

# Vectores de la misma longitud

print(Ages + Ages)

print(Ages * Ages)

print ('*********************************************************************************') 

# Vector con enteros (escalares)

print(Ages + 100)

print()

print (Ages * 2)
print()

print(Ages + pd.Series([1, 100]))

print()

print(Ages)
print ('*********************************************************************************') 


# Vector con etiquetas de índice comunes (alineación automática)

rev_Ages = Ages.sort_index(ascending=False)
print(rev_Ages)

# Salida de referencia para mostrar la alineación de la etiqueta de índice

print (Ages * 2)

print (Ages + rev_Ages)

# Los vectores booleanos formarán subconjuntos de filas


print(cientificos[cientificos['Edad'] > cientificos['Edad'].mean()])

print ('*********************************************************************************') 


# 4 values passed as bool vector
# 3 rows returned 

print (cientificos.loc[[True, True, False, True]])

print ()

First_half = cientificos [:4]
second_half = cientificos [4:]

print (First_half)

print (second_half)

# Multiplica por una escalar

print(cientificos * 2)

print ('*********************************************************************************') 

# Agregar columnas adicionales

print(cientificos['Nacimiento']. dtype)

print(cientificos['Muerte']. dtype)

# Dar formato a la columna 'Nacido' como fecha y hora

Nacimiento_datetime = pd.to_datetime(cientificos['Nacimiento'], format= '%Y-%m-%d')

print(Nacimiento_datetime)

print()

Muerte_datetime = pd.to_datetime(cientificos['Muerte'], format= '%Y-%m-%d')

cientificos['Nacimiento_dt'], cientificos['Muerte_dt'] = (Nacimiento_datetime, Muerte_datetime)

print(cientificos.head())

print(cientificos.shape)

print ('*********************************************************************************') 

# Cambiar directamente una columna

print(cientificos['Edad'])
print()

cientificos['Edad_days_dt'] = (cientificos['Muerte_dt'] - cientificos['Nacimiento_dt'])


print ('*********************************************************************************') 

# Todas las columnas actuales en nuestros datos

print (cientificos .columns)

# Columnas después de quitar la columna de edad

print()
cientificos_dropped = cientificos.drop(['Edad'], axis=1)

# columnas después de dejar caer nuestra columna

print(cientificos_dropped.columns)
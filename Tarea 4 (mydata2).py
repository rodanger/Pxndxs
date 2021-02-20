import pandas as pd, numpy as np
 
from collections import OrderedDict

# Creando nuestra data

print()

print ('*********************************************************************************') 

print()

c = pd.Series (['Joe lopez', 'DevOp'], index = ['Persona', 'Who']) # Declaramos la variable que contendra las series

print (c) 

print()

print ('*********************************************************************************')

print()

# Creando nuestro DataFrame 

c = pd.DataFrame( 
    data = {'Ocupacion': ['Ing. Quimico' , 'Astronomo', 'Bioquimico' , 'Biofisico'] ,
     'Nacimiento': ['1971-08-23' , '1983-03-13' , '1975-04-11' , '1988-04-27'] ,
     'Muerte': ['2014-02-23' , '2019-05-24' , '2010-08-29' , '2017-10-17'] ,
      'Edad' : [43, 36, 35, 29 ]} ,
       index =  ['Andrea Castro' , 'Carlos de la rosa' , 'Jose Matos' , 'Carla Martinez' ] ,
     columns = ['Ocupacion' , 'Nacimiento' , 'Muerte' , 'Edad'])

print () 

print ('*********************************************************************************')

#Seleccionar por etiqueta de índice de fila

primera_fila = c.loc ['Andrea Castro']

print (type(primera_fila))

print('***********************************************')

segunda_fila = c.loc ['Jose Matos']

print (type(segunda_fila))

print('***********************************************')

print (primera_fila)

print()

print (segunda_fila)


# Creando nuestra data

print()

print ('*********************************************************************************') 

print()



print ('*********************************************************************************')

print()

# Creando nuestro DataFrame 


print ('*********************************************************************************')

#Seleccionar por etiqueta de índice de fila

primera_fila = c.loc ['Andrea Castro']

print (type(primera_fila))

print('***********************************************')

segunda_fila = c.loc ['Jose Matos']

print (type(segunda_fila))

print('***********************************************')

print (primera_fila)

print()

print (segunda_fila)

print ('*********************************************************************************')     
print ()

Ages = c['Edad']

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

print()

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


print(c[c['Edad'] > c['Edad'].mean()])

print ('*********************************************************************************') 


# 4 valores pasados como vector bool
# 3 filas devueltas 

print (c.loc[[True, True, False, True]])

print ()

First_half = c [:4]
second_half = c [4:]

print (First_half)

print (second_half)

# Multiplica por una escalar

print(c * 2)

print ('*********************************************************************************') 

# Agregar columnas adicionales

print(c['Nacimiento']. dtype)

print(c['Muerte']. dtype)

# Dar formato a la columna 'Nacido' como fecha y hora
print ('*********************************************************************************') 

Nacimiento_datetime = pd.to_datetime(c['Nacimiento'], format= '%Y-%m-%d')

print(Nacimiento_datetime)

print()

Muerte_datetime = pd.to_datetime(c['Muerte'], format= '%Y-%m-%d')

c['Nacimiento_dt'], c['Muerte_dt'] = (Nacimiento_datetime, Muerte_datetime)

print ()

print('**********************************************************************************')

print(c.head())

print(c.shape)

print ('*********************************************************************************') 

# Cambiar directamente una columna

print(c['Edad'])
print()

print ('*********************************************************************************') 


c['Edad_days_dt'] = (c['Muerte_dt'] - c['Nacimiento_dt'])

print()

print ('*********************************************************************************') 

# Todas las columnas actuales en nuestros datos

print (c.columns)

# Columnas después de quitar la columna de edad

print ('*********************************************************************************') 

print()

c_dropped = c.drop(['Edad'], axis=1)

# columnas después de dejar caer nuestra columna

print(c_dropped.columns)

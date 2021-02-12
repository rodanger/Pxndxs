import pandas as pd 

from collections import OrderedDict

# Creando nuestra data
print ('*********************************************************************************') 

c = pd.Series (['Joe lopez', 'DevOp'], index = ['Persona', 'Who']) # Declaramos la variable que contendra las series

print (c) 

print ('*********************************************************************************')
# Creando un DataFrame

d = pd.DataFrame ({'Nombre': ['Andrea Castro' , 'Carlos de la rosa' ] ,
 'Ocupacion': ['Ing. Quimico' , 'Pedriatra'] , 'Nacimiento': ['1971-08-23' , '1983-03-13'] ,
 'Muerte' : ['2014-02-23' , '2019-05-24'] , 'Edad' : [43, 36]})
print (d)

print ('*********************************************************************************')


# Creando nuestro ejemplo de DataFrame 
# Con una columna indexando etiqueta 


print ('*********************************************************************************')


cientificos = pd.DataFrame( 
    data = {'Ocupacion': ['Ing. Quimico' , 'Pedriatra'] ,
     'Nacimiento': ['1971-08-23' , '1983-03-13'] ,
     'Muerte': ['2014-02-23' , '2019-05-24'] ,
      'Edad' : [43, 36]} ,
       index =  ['Andrea Castro' , 'Carlos de la rosa' ] ,
     columns = ['Ocupacion' , 'Nacimiento' , 'Muerte' , 'Edad'])

print (cientificos) 

print ('*********************************************************************************')

#Seleccionar por etiqueta de índice de fila

primera_fila = cientificos.loc ['Carlos de la rosa']
print (type(primera_fila))

print (primera_fila)

print ('*********************************************************************************')
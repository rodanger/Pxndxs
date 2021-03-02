import pandas as pd

df1 = pd.read_csv('concat_1.csv') # Leyendo archivo CSV
print(df1)

print ('*********************************************************************************') 

print()

df2 = pd.read_csv('concat_2.csv') # Leyendo archivo CSV
print(df2)

print()

print ('*********************************************************************************') 

print()
df3 = pd.read_csv('concat_3.csv') # Leyendo archivo CSV

print(df3)


print()

print ('*********************************************************************************') 

print()

row_concat = pd.concat([df1, df2, df3])
print(row_concat)

print ('*********************************************************************************') 

print()


# Subconjunto de la cuarta fila si el marco de datos concatenado

print(row_concat.iloc[3, ])


print()

# Creando una nueva fila de datos

new_row_series = pd.Series(['n1' , 'n2' , 'n3' , 'n4'])

print(new_row_series)

print ('*********************************************************************************')

print()

#nueva fila a un marco de datos

print(pd.concat([df1 , new_row_series]))


new_row_df = pd.DataFrame([['n1' , 'n2' , 'n3' , 'n4' ]],
columns=['A', 'B', 'C', 'D'])

print(new_row_df)

print()

print ('*********************************************************************************')

print(df1)

print()

print(pd.concat([df1, new_row_df]))

# Usando un marco de datos

print(df1.append(df2))

# Usando un DataFrame de una sola fila

print(df1.append(new_row_df))


data_dict = {'A': 'n1',
             'B': 'n2',
             'C': 'n3',
             'D': 'n4'}  

# Usando el diccionario de Python

print(df1.append(data_dict, ignore_index=True))             

print()

print ('*********************************************************************************')
# Ignorando el índice

row_concat_i = pd.concat([df1 ,df2, df3], ignore_index=True)
print(row_concat_i)

print()
print()

# Agregando columnas
col_concat = pd.concat([df1, df2, df3], axis=1)
print(col_concat)

print()

print ('*********************************************************************************')

# Agregando una sola columna a un marco de datos

col_concat['new_col_list'] = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(col_concat)
 
print()

print ('*********************************************************************************')

# El uso de la función concat sigue funcionando

col_concat['new_col_series'] = pd.Series(['n1', 'n2', 'n3', 'n4'])
print(col_concat)

print()

# El uso de la función concat sigue funcionando

print(pd.concat([df1, df2, df3], axis=1, ignore_index=True))


print ('*********************************************************************************')
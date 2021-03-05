import pandas as pd 

df1 = pd.read_csv('concat_1.csv')
df2 = pd.read_csv('concat_2.csv')
df3 = pd.read_csv('concat_3.csv')

# Concatenando filas con columnas

df1.columns = ['A', 'B', 'C', 'D']
df2.columns = ['E', 'F', 'G', 'H']
df3.columns = ['A', 'C', 'F', 'H']

print(df1)
print()

print(df2) 
print()

print(df3)
print()

print ('*********************************************************************************')

# Las columnas se alinean y NaN rellena las áreas faltantes

row_concat = pd.concat([df1, df2, df3])
print(row_concat)


print(pd.concat([df1, df2, df3], join='inner'))

print(pd.concat)


# Solo se devolverán las columnas que todos comparten

print(pd.concat([df1, df3], ignore_index=False, join='inner'))

### Concatenar columnas con diferentes filas

df1.index = [0, 1, 2, 3]
df2.index = [4, 5, 6, 7]
df3.index = [0, 2, 5, 7]

print(df1)
print()

print(df2)
print()

print(df3)
print()

print ('*********************************************************************************')

col_concat = pd.concat([df1, df2, df3], axis=1)
print(col_concat)

print()

print ('*********************************************************************************')

print(pd.concat([df1,df3], axis=1, join='inner'))

import pandas as pd

df1 = pd.read_csv('concat_1.csv')
print(df1)

print ('*********************************************************************************') 

print()

df2 = pd.read_csv('concat_2.csv')
print(df2)

print()

print ('*********************************************************************************') 

print()
df3 = pd.read_csv('concat_3.csv')

print(df3)


print()

print ('*********************************************************************************') 

print()
row_concat = pd.concat([df1, df2, df3])

print(row_concat)

print ('*********************************************************************************') 

print()


# Subset the fourth row if the concatenated dataframe
print(row_concat.iloc[3, ])


print()



# Create a new row of data

new_row_series = pd.Series(['n1' , 'n2' , 'n3' , 'n4'])

print(new_row_series)

print ('*********************************************************************************')

print()

# Attempt to add the new row to a dataframe
print(pd.concat([df1 , new_row_series]))


# Note the double brackets

new_row_df = pd.DataFrame([['n1' , 'n2' , 'n3' , 'n4' ]],
columns=['A', 'B', 'C', 'D'])

print(new_row_df)

print()

print ('*********************************************************************************')
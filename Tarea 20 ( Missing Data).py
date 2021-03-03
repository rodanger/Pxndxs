import pandas as pd
from numpy import NaN, NaN, nan


visited = pd.read_csv('survey_visited.csv')
survey = pd.read_csv('survey_survey.csv')

print ('*********************************************************************************')

print ()

print(visited)

print()

print(survey)

print()

vs = visited.merge(survey, left_on='ident', right_on='taken')

print(vs)


print()

print ('*********************************************************************************')

# Falta valor en una serie

num_legs = pd.Series({'goat': 4, 'amoeba': nan})
print(num_legs)

print()

# Falta valor en un marco de datos

scientists = pd.DataFrame({
    'name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation':['Chemist', 'Statistician'],
    'Born':['1920-07-25', '1876-06-13'],
    'Died':['1958-04-16', '1937-10-16'],
    'Missing': [nan, nan]})

print(scientists)    

print()

print ('*********************************************************************************')

# Crea un nuevo marco de datos

scientists = scientists = pd.DataFrame({
    'name': ['Rosaline Franklin', 'William Gosset'],
    'Occupation':['Chemist', 'Statistician'],
    'Born':['1920-07-25', '1876-06-13'],
    'Died':['1958-04-16', '1937-10-16']})


print()

print ('*********************************************************************************')
# Asignar una columna de valores perdidos
scientists['missing'] = nan
print(scientists)

print()

gapminder = pd.read_csv('gapminder.tsv', sep='\t')

life_exp = gapminder.groupby(['year'])['lifeExp'].mean()
print(life_exp)

print()

# Subset

print()

y2000 = life_exp[life_exp.index > 2000]
print(y2000)

print()

# Reindex

print(y2000.reindex(range(2000, 2010)))

print()

print ('*********************************************************************************')
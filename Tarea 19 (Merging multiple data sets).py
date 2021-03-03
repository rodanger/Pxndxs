import pandas as pd 

df1 = pd.read_csv('concat_1.csv')
df2 = pd.read_csv('concat_2.csv')
df3 = pd.read_csv('concat_3.csv')

person = pd.read_csv('survey_person.csv')
site = pd.read_csv('survey_site.csv')
visited = pd.read_csv('survey_visited.csv')
survey = pd.read_csv('survey_survey.csv')

# Fusión uno a uno

visited_subset = visited.loc[[0, 2, 6]]

print()

# El valor predeterminado para 'cómo' es 'interno'
# Por lo que no es necesario especificarlo

o2o_merge = site.merge(visited_subset,
                       left_on='name', right_on='site')
print(o2o_merge)                       

print()

# Muchos a uno se fusionan

m2o_merge = site.merge(visited, left_on='name', right_on='site')
print(m2o_merge)

print()

# Muchos a muchos se fusionan

ps = person.merge(survey, left_on='ident', right_on='person')
vs = visited.merge(survey, left_on='ident', right_on= 'taken')

print (ps)

print()


print(vs)

# Multiples columnas para hacer coincidir en una lista de Python

print()


ps_vs = ps.merge(vs, 
                 left_on=['ident', 'taken', 'quant', 'reading'],
                 right_on=['person', 'ident', 'quant', 'reading'])

print(ps_vs.loc[0, ])                 
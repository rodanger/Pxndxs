import seaborn as sns, matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # Cargamos el dataset Tips

count, ax = plt.subplots() 

ax = sns.countplot('day', data=tips) # Permite usar gráficos para contar variables discretas
ax.set_title('Count of days') # Titulo del histograma
ax.set_xlabel('Day of the week') # x sera Day of week
ax.set_ylabel('Frecuency') # y sera Frecuency
 
#Mostramos el grafico
plt.show()


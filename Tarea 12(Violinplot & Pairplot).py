import seaborn as sns, matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # Cargamos el dataset Tips


### Violin Plot

violin, ax = plt.subplots()

ax = sns.violinplot(x='time', y='total_bill', data=tips)

ax.set_title('Violin plot of total of total bill by time of day') # Titulo del ViolinPlot
ax.set_xlabel('Time of day') # La etiqueta x sera 'Time of date'
ax.set_ylabel('Total Bill') # La etiqueta y sera 'Total Bill


plt.show() # Mostrar grafico 


pair_grid = sns.PairGrid(tips) # Cuadrícula de subparcelas para trazar relaciones por pares en un conjunto de datos.

pair_grid = pair_grid.map_upper(sns.regplot) #
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.distplot, rug=True)

plt.show() # Mostrar grafico


violin, ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)
plt.show()

scatter = sns.lmplot(x='total_bill', y ='tip' , data=tips, hue='sex', fit_reg=False)
plt.show() #Mostrar grafico


### Pairplot

fig = sns.pairplot(tips, hue= 'sex')

scatter = sns.lmplot(x='total_bill', y= 'tip', data=tips,
fit_reg=False, hue='sex',markers=['o', 'x'],
scatter_kws={'s': tips['size']*10})

plt.show() # Mostrar grafico
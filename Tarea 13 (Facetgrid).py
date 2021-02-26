import seaborn as sns, matplotlib.pyplot as plt

anscombe = sns.load_dataset('anscombe') # Cargamos el dataset Tips
tips = sns.load_dataset('tips')

anscombe_plot = sns.lmplot(x='x', y='y' , data=anscombe , 
                           fit_reg=False,
                           col='dataset', col_wrap=2)


facet = sns.FacetGrid(tips, col='time')


facet.map(sns.distplot, 'total_bill' , rug=True)

plt.show() #Mostrar grafico I
 
facet = sns.FacetGrid(tips, col='day' , hue='sex')
facet = facet.map(plt.scatter, 'total_bill', 'tip')
facet = facet.add_legend()

plt.show() # Mostrar grafico II

facet = sns.FacetGrid(tips, col='time', row='smoker', hue='sex')
facet.map(plt.scatter, 'total_bill' , 'tip')

plt.show() # Mostrar grafico III




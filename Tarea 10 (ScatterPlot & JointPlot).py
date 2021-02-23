import seaborn as sns, matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # Cargamos el dataset Tips

scatter, ax = plt.subplots()
ax = sns.regplot(x = 'total_bill', y = 'tip', data=tips) 
ax.set_title('Scatterplot of Total Bill and Tip') # Titulo del regplot
ax.set_xlabel('Total Bill') # x sera Total Bill 
ax.set_ylabel('Tip') # y sera Tip

# Mostrar grafico
plt.show() 


fig = sns.lmplot(x ='total_bill', y = 'tip', data = tips)

# Mostrar grafico
plt.show()


joint = sns.jointplot(x = 'total_bill', y = 'tip', data = tips)
joint.set_axis_labels(xlabel= 'Total Bill', ylabel= 'Tip')

# Agregando  título, colocando el tamaño de fuente y moviendo el siguiente por encima del total de ejes de la factura
joint.fig .suptitle('Joint Plot of Total Bill and Tip', fontsize=10, y=1.03)

# Mostrar Grafico
plt.show()

# Hexbin Plot usando jointplot

hexbin = sns.jointplot(x= 'total_bill', y = 'tip', data = tips, kind='hex')
hexbin.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip', fontsize=10,  y=10.3)

# Mostrar Grafico
plt.show()

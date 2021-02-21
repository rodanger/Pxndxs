import matplotlib.pyplot as plt,  seaborn as sns 


# Creando el histograma 
tips = sns.load_dataset ("tips") # Cargamos nuestro dataset
print(tips.head())


print()

fig = plt.figure()
axes1 = fig.add_subplot(1, 1, 1)
axes1.hist(tips[ 'total_bill' ], bins =10)
axes1.set_title('Histogram of Total Bill') # Titulo del histograma

axes1.set_xlabel('Frecuency') # En x se encontrara la frecuencia
axes1.set_ylabel('Total Bill') # En y estara Total Bill

# Mostramos el grafico
fig.show()
plt.show() 


### Boxplot

scatter_plot = plt.figure()

axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(tips['total_bill'], tips['tip'])
axes1.set_title('Scatterplot of Total Bill vs Tip') # Titulo del histograma
axes1.set_xlabel('Total Bill') # x sera Total Bill
axes1.set_ylabel('tip') # y sera tip

# Mostramos el grafico
plt.show()

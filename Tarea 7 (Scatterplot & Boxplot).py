import pandas as pd, matplotlib.pyplot as plt, numpy as np, seaborn as sns 


tips = sns.load_dataset ("tips") # Cargamos nuestro dataset
print(tips.head())



### Boxplot

scatter_plot = plt.figure()

axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(tips['total_bill'], tips['tip'])
axes1.set_title('Scatterplot of Total Bill vs Tip') # Titulo de la subtrama
axes1.set_xlabel('Total Bill') # x sera Total Bill
axes1.set_ylabel('tip') # y sera tip

plt.show() # Desplegar el plot 

# Boxplot de tipos por sexo

boxplot = plt.figure()

axes1 = boxplot.add_subplot(1, 1, 1)
axes1.boxplot(

    # El primer argumento de boxplot son los datos
    # Dado que estamos trazando varios datos
    # Tenemos que poner cada dato en una lista

    [tips[tips['sex'] == 'Female']['tip'] ,
    tips[tips['sex'] == 'Male']['tip']] ,

    # Pasando un parámetro de etiquetas 

    labels =['Female', 'Male'])
axes1.set_xlabel('Sex')
axes1.set_ylabel('Tip')
axes1.set_title('Boxplot of Tips by Sex')

boxplot.show()
plt.show()


# Creando una variable de color basada en el sexo

def recode_sex(sex):
 if sex == 'female':
    return 0

 else: 
     return 1


tips['sex_color'] = tips['sex'].apply(recode_sex)

scatter_plot = plt.figure()
axes1 = scatter_plot.add_subplot(1, 1, 1)
axes1.scatter(
    x= tips['total_bill'],
    y= tips['tip'],

    s = tips['size'] * 10, # se multiplica el tamaño * 10

    c = tips['sex_color'],
    
    alpha=0.5)

axes1.set_title('Total Bill vs Tip Colored by Sex and Sized by Size ') # Titulo del subplot
axes1.set_xlabel('Total Bill') # La etiqueta x sera 'Total Bill'
axes1.set_ylabel('Tip') # La etiqueta y sera 'Tip'

# Desplegamos el grafico
scatter_plot.show()
plt.show()



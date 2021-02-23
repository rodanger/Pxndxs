import seaborn as sns, matplotlib.pyplot as plt

tips = sns.load_dataset('tips')# Cargamos nuestro dataset


### 2D Density Plot
kde = plt.subplots()
ax = sns.kdeplot(data=tips['total_bill'], data2=tips['tip'], shade=True) # La sombra llenará los contornos
ax.set_title('Kernel Density Plot of Total Bill and Tip') # Titulo del kdeplot
ax.set_xlabel('Total Bill') # x sera Total Bill 
ax.set_ylabel('tip') # y sera tip
 
plt.show() # Mostrar grafico


kde_jointplot = sns.jointplot(x='total_bill', y = 'tip', data=tips, kind='kde')


plt.show() # Mostrar grafico


### Bar Plot  

bar, ax = plt.subplots()
ax = sns.barplot(x='time' , y= 'total_bill' , data=tips) # en el barplot x sera el tiempo , y total_bill
ax.set_title('Bar Plot of average total bill for time of day') # Titulo del barplot
ax.set_xlabel('Time of day') # la etiqueta de x sera 'Time of day'
ax.set_ylabel('Average total bill') # la etiqueta de y sera 'Average total bill'

plt.show() # Mostrar grafico


### Boxplot

box, ax = plt.subplots()
ax = sns.boxplot(x= 'time', y='total_bill', data=tips) # en el boxplot x sera 'time' , y sera total_bill
ax.set_title('Boxplot of Total Bill by time of day') # titulo del Boxplot
ax.set_xlabel('Time of Day') # la etiqueta de x es 'Time of Day'
ax.set_ylabel('Total Bill') # la etiqueta de y es 'Total Bill'

plt.show() # Mostrar grafico


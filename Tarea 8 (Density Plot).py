mport seaborn as sns 
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # Cargamos nuestro dataset

# Esta función de subtramas es un atajo
# para crea un objeto de figura separada y
# agregar subparcelas individuales (ejes) a la figura

hist,ax = plt.subplots()

# Usando la función distplot de seaborn para crear nuestro gráfico

ax = sns.distplot(tips['total_bill'])
ax.set_title('Total Bill Histogram with Density Plot')

plt.show() # Mostrar grafico

### Histograma de Total Bill con plot de densidad

hist, ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], kde=False) # Parámetro kde = falso
ax.set_title('Total Bill Histogram') # Titulo del histograma
ax.set_xlabel('Total Bill') # x sera Total Bill
ax.set_ylabel('Frecuency') # y sera la frecuencia

plt.show() # Mostrar grafico 


### Histograma de Total Bill

den, ax = plt.subplots() 
ax = sns.distplot(tips['total_bill'], hist=False) # Parametro kde = falso
ax.set_title('Total Bill Density') # Titulo de historigrama
ax.set_xlabel('Total Bill') # x sera Total Bill
ax.set_ylabel('Unit Probability') # y sera Unit Probability

plt.show() # Mostrar grafico


### Histograma de factura total con densidad y trazado de alfombra

hist_den_rug, ax = plt.subplots() 
ax = sns.distplot(tips['total_bill'], rug=True) # parametro alfombra = True
ax.set_title('Total Bill Density and Rug Plot') # titulo del historigrama
ax.set_xlabel('Total Bill') # x sera Total Bill

plt.show() # Mostrar grafico
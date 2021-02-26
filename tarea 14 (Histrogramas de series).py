import seaborn as sns, matplotlib.pyplot as plt 

anscombe = sns.load_dataset('anscombe') # Cargamos el dataset Tips
tips = sns.load_dataset('tips')

### Histograma de serie Pandas

# En una serie

fig, ax = plt.subplots()

ax = tips['total_bill'].plot.hist()

plt.show() # Mostrar grafico


# en un marco de datos
# establecer una transparencia de canal alfa
# para que podamos ver las barras superpuestas


fig, ax = plt.subplots()
ax = tips[['total_bill', 'tip']].plot.hist(alpha=0.5, bins=20 , ax=ax)

plt.show() # Mostrar grafico


fig, ax = plt.subplots()
ax = tips['tip'].plot.kde()

plt.show() # Mostrar grafico


fig, ax = plt.subplots()
ax = tips.plot.scatter(x='total_bill' , y ='tip', ax=ax)

plt.show() # Mostrar grafico


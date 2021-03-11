import matplotlib.pyplot as plt

import seaborn as sns 

anscombe = sns.load_dataset("anscombe")

print(anscombe)


# Creando un subconjunto de los datos
# Contiene solo el conjunto de datos 1 de anscombe
 
dataset_1 = anscombe[anscombe['dataset'] == 'I' ]

plt.plot(dataset_1['x'], dataset_1['y'])

plt.plot(dataset_1['x'], dataset_1['y'], 'o')


# Creando subconjuntos de datos de anscombe

dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']

# Creando la figura completa donde irán nuestras subtramas
fig = plt.figure()

# 2 hileras del plot y cada fila tendrá 2 plot

# El subplot tiene 2 filas y 2 columnas, ubicación del plot 1
axes1 = fig.add_subplot(2, 2, 1)

# El subplot tiene 2 filas y 2 columnas, ubicación del plot 2
axes2 = fig.add_subplot(2, 2, 2)

# El Subplot tiene 2 filas y 2 columnas, ubicación del plot 3
axes3 = fig.add_subplot(2, 2, 3)

# El Subplot tiene 2 filas y 2 columnas, ubicación del plot 4
axes4 = fig.add_subplot(2, 2, 4)


# Agregando un gráfico a cada uno de los ejes creados anteriormente

axes1.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

# Agregando un pequeño título a cada subtrama
axes1.set_title("dataset_1")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")

# Agregando un título para la figura completa
fig.suptitle("Anscombe Data")

# Diseño ajustado
fig.tight_layout()

# Mostrar el plot
plt.show()

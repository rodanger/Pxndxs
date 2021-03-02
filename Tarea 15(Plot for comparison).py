import seaborn as sns, matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Initial plot for comparison
fig, ax = plt.subplots()
ax = sns.violinplot(x='time' , y='total_bill', hue='sex', data=tips, split=True)

plt.show() # Mostrar grafico

# set style and plot 
sns.set_style('whitegrid')
fig, ax = plt.subplots()
ax = sns.violinplot(x='time' , y='total_bill', hue='sex', data=tips, split=True)


plt.show() # Mostrar grafico


fig = plt.figure()

seaborn_styles =['darkgrid', 'whitegrid', 'dark', 'white', 'ticks'] # Titulos de los plots

for idx, style in enumerate(seaborn_styles):
    plot_position = idx + 1

    with sns.axes_style(style):

     ax = fig.add_subplot(2, 3, plot_position)
     violin = sns.violinplot(x='time', y='total_bill', 
                             data=tips, ax=ax)
     violin.set_title(style)
fig.tight_layout()


plt.show() # Mostrar grafico
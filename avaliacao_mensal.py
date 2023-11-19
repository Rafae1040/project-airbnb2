colunas = 'reviews_per_month'
linhas = data.loc[:, 'reviews_per_month'] < 10
data_plot = data.loc[linhas, colunas]

plt.hist( data_plot, bins=10, edgecolor= 'black')
plt.title( 'Numero de Avaliações por Mês');
plt.xlabel( 'Quantidade de Avaliações');
plt.ylabel( 'Quantidade de Imóveis');
plt.grid(True)
plt.show()


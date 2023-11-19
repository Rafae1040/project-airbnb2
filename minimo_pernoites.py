linhas = data.loc[:, 'minimum_nights'] < 100

minimum_nights = data.loc[linhas, 'minimum_nights']

plt.hist(minimum_nights, bins=20, edgecolor='black')
plt.xlabel('Minimo de Noites')
plt.ylabel('Quantidade de Imoveis')
plt.title('Minimo de Noites por Imoveis')
plt.grid(True)
plt.show()

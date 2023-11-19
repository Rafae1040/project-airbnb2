linhas = data.loc[:, 'price'] < 1100
price = data.loc[linhas,'price']

# maior valor de aluguel
print('O maior valor de aluguel: {}'.format(np.max(price)))

# histograma
plt.hist(price, bins=11, edgecolor='black') # ajusta o número de intervalos e a cor da borda
plt.xlabel('Valor de Aluguel')
plt.ylabel('Quantidade de Imoveis')
plt.title('Valor de Aluguel dos Imoveis')
plt.grid(True)
plt.show()

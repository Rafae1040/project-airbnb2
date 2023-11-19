linhas = data.loc[:, 'number_of_reviews'] < 300

number_of_reviews = data.loc[linhas, 'number_of_reviews']

plt.hist(number_of_reviews, bins=12, edgecolor='black')
plt.xlabel('Numeros de Reviews')
plt.ylabel('Quantidade de Imoveis')
plt.title('Avaliação dos Imoveis')
plt.grid(True)
plt.show()


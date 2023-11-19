colunas = 'price'

media = data.loc[:, colunas].mean()
desvio_padrao = (data.loc[:, colunas]).std()

print(' O preco medio de aluguel em NY eh U${:.2f} +/- U${:.2f}'.format(media, desvio_padrao))

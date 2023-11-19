# seleção de colunas e linhas
host_id = data.loc[:, 'host_id']

# separação dos valores unicos
host_id_unique =  np.unique(host_id)

# contagem dos valores unicos
len( host_id_unique )
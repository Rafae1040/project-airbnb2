# Importando as Bibliotecas 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.read_csv('/content/AB_NYC_2019.csv')

# Consultando linhas e colunas
data.info()

data.head()
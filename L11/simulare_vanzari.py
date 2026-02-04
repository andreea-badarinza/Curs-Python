import numpy as np
import pandas as pd
import random

# Generare 60 de zile
zile = pd.date_range(start='2024-01-01', periods=60)
produse = ['ProdusA', 'ProdusB', 'ProdusC', 'ProdusD', 'ProdusE']

data_list = []

for zi in zile:
    nr_produse = random.randint(5, 15)  # Număr aleator de produse pe zi
    produse_zi = np.random.choice(produse, size=nr_produse)

    for produs in produse_zi:
        pret = np.random.normal(40, 8)  # Preț normal medie=40, dev=8
        cantitate = np.random.randint(1, 11)  # Cantitate între 1-10
        promotie = np.random.rand() < 0.3  # 30% șanse de promoție
        if promotie:
            pret *= 0.8  # Reducere 20%
        venit = pret * cantitate
        profit = venit * 0.3  # Marja profit 30%
        data_list.append([zi, produs, cantitate, round(pret, 2), round(venit, 2), round(profit, 2), promotie])

# Creare DataFrame
df_sim = pd.DataFrame(data_list, columns=['data', 'produs', 'cantitate', 'pret', 'venit', 'profit', 'promotie'])

# Vizualizare primele rânduri
print(df_sim.head())

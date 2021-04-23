import numpy as np
from data.datamanager import data_loader

path = './data/adult_test.csv'
x, y = data_loader(path)

print(x[:1])
print(x.loc[x['race'] == "White"][:2])

n_whites = len(x.loc[x['race'] == "White"])
print(n_whites)




import numpy as np

getallen = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        getallen[i,j] = i*j

print(getallen)
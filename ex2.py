# Crie uma matriz numpy3x3 com valores aleatórios entre 0 e 10. Dica: use np.random.rand()

import numpy as np

arr = np.random.randint(low=0, high=10, size=(3, 3))
print(arr)

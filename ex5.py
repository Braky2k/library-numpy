# Transponha uma matriz. Exemplo: Seja matriz = np.array([[1, 2], [3, 4], [5, 6]]), o resultado seria array([[1, 3, 5], [2, 4, 6]])

import numpy as np

# Criando array
matriz = np.array([[1, 2], [3, 4], [5, 6]])
# .T parâmetro para transportar uma array.
transp = matriz.T
# Imprimindo
print(transp)

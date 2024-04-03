# Concatene duas matrizes horizontalmente. Dica: use np.hstack()

import numpy as np

# Criando array 1
mtz1 = np.array([[1, 2, 3], [4, 5, 6]])
# Criando array 2
mtz2 = np.array([[7, 8, 9], [10, 11, 12]])

# hstack(()) responsável por juntar vetores de array da mesma escala e compor com outras matrizes diferentes.
arr = np.hstack((mtz1, mtz2))
# Imprimindo
print(arr)

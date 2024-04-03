# Converta uma matriz em um vetor unidimensional. Exemplo: Seja matriz = np.array([[1, 2, 3], [4, 5, 6]]), o resultado seria array([1, 2, 3, 4, 5, 6])

import numpy as np

# Criando array
matriz = np.array([[1, 2, 3], [4, 5, 6]])
# Parâmetro para transportar uma array para 1 Dimensão.
ajuste = matriz.reshape(-1)
# Imprimindo
print(ajuste)

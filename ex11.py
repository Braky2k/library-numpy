# Reshape um vetor unidimensional em uma matriz 3x3. Exemplo: Seja vetor = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), o resultado seria array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

import numpy as np

# Criando Array
vetor = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# Convertendo para matriz 3x3
convert = vetor.reshape(3, 3)
# Imprimindo
print(convert)

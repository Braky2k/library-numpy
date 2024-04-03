# Calcule a soma cumulativa de um vetor. Dica: usar np.cumsum() Exemplo: Seja vetor = np.array([1, 2, 3, 4]), o resultado seria array([ 1, 3, 6, 10])

import numpy as np

# Criando array
vetor = np.array([1, 2, 3, 4])
# np.cumsum() Soma o valor do índice n com seus valores anteriores.
soma = np.cumsum(vetor)
# Imprimindo
print(soma)

# Multiplique os elementos de uma matriz por uma constante de forma que a matriz resultante tenha a soma de todos os seus elementos igual a 1. Não usar loops. Exemplo: Seja matriz = np.array([[1, 2], [3, 4]]), o resultado seria array([[0.1, 0.2], [0.3, 0.4]]).

import numpy as np

# Criando array
matriz = np.array([[1, 2], [3, 4]])
# Soma dos elementos da matriz
soma = np.sum(matriz)
# 1 Dividido pela soma, multiplica pelo elemento da matriz no qual resulta o valor, que no total será 1.
vetor = matriz * (1 / soma)
# Imprimindo
print(vetor)

# Multiplique uma matriz por um vetor. Exemplo: Seja matriz = np.array([[1, 2], [3, 4]]) e vetor = np.array([5, 6]), o resultado seria array([17, 39])

import numpy as np

# Criando array
matriz = np.array([[1, 2], [3, 4]])
# Criando Multiplicador
vetor = np.array([5, 6])
# Parâmetro sum para somar as matrizes. Axis é responsável por modelar o formato para calcular individualmente, e não em conjunto.
soma = np.sum(matriz * vetor, axis=1)
# Imprimindo
print(soma)

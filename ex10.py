# Substitua todos os valores negativos em um vetor por 0. Exemplo: Seja vetor = np.array([-1, 2, -3, 4, -5]), o resultado seria array([0, 2, 0, 4, 0])

import numpy as np

# Criando array
vetor = np.array([-1, 2, -3, 4, -5])
# Para toda numeração negativa recebe o valor 0.
vetor[vetor < 0] = 0
# Imprimindo
print(vetor)

# Calcule a média e o desvio padrão de cada linha de uma matriz. Dica: use np.mean() e np.std(). Exemplo: matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). O resultado deve ser: média por linha: [2. 5. 8.], desvio padrão por linha: [0.8165, 0.8165, 0.8165]

import numpy as np

# Criando array
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# np.mean() responsável por calcular a média.
media = np.mean(matriz, axis=1)
# np.std() responsável por calcular o desvio padrão.
dpadrao = np.std(matriz, axis=1)
# Imprindo valores
print('\033[1mMédia por linha:\033[0m', media, '\n\033[1mDesvio Padrão:\033[0m', dpadrao)
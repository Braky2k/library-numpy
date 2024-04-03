# Calcule a média e o desvio padrão de cada coluna de uma matriz. Dica: use np.mean() e np.std(). Exemplo: matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]). O resultado deve ser: média por coluna: [4. 5. 6.], desvio padrão por coluna: [2.4495, 2.4495, 2.4495]

import numpy as np

# Criando array
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# .T parâmetro igual à np.transpose(), responsável por fazer transposta na matriz.
m = matriz.T
# np.mean() responsável por calcular a média.
mediaT = np.mean(m, axis=1)
# np.std() responsável por calcular o desvio padrão.
desvioT = np.std(m, axis=1)
# Imprimindo
print('\033[1mMédia por coluna:\033[0m', mediaT, '\n\033[1mDesvio Padrão:\033[0m', desvioT )

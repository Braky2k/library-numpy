# Encontre o produto escalar entre os vetores [1, 2, 3] e [4, 5, 6]. Dica: use np.dot() e também o operador @ para conferir o outro resultado

import numpy as np

# Criando array 1
arr1 = np.array([1, 2, 3])
# Criando array 2
arr2 = np.array([4, 5, 6])

# @ Mesma função do .dot(), responsável por multiplicar os dados e somar.
relation = arr1 @ arr2
# Imprimindo
print(relation)

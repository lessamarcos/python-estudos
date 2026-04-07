import numpy as np

arr = np.arange(1, 21, 1)
print(f"Array completo: {arr}")
print(f"Array shape: {arr.shape}")
print(f"Array soma: {arr.sum()}")
print(f"Array média: {arr.mean()}")
print(f"Array máximo: {arr.max()}")
print(f"Array mínimo: {arr.min()}")
print(f"Array desvio padrão: {arr.std()}")
print(arr[arr % 2 == 0])

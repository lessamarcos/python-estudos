import numpy as np

matriz = np.arange(1, 10).reshape(3, 3)

print(f"Soma de todos os elementos: {matriz.sum()}")
print(f"Media linha: {matriz.mean(axis=1)}")
print(f"Media coluna: {matriz.mean(axis=0)}")
print(f"Shape: {matriz.shape}")
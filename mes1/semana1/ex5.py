import numpy as np

arr1 = np.arange(1, 5)
arr2 = np.arange(5, 9)
matriz = np.vstack([arr1, arr2])
print(f"Matriz {matriz}")
print(f"Shape: {matriz.shape}")
print(f"Soma Coluna: {matriz.sum(axis=0)}")
print(f"Matriz transposta: {matriz.T}")
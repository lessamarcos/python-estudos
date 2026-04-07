import numpy as np

arr = np.random.randint(1, 101, 50)

print(f"Média: {arr.mean()} Máximo: {arr.max()} Mínimo: {arr.min()}")
print(f"A quantidade de valores maiores que a média são: {len(arr[arr > arr.mean()])}")
arr = (arr - arr.min()) / (arr.max() - arr.min())
print(arr.round(2))
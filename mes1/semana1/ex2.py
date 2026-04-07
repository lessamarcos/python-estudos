import numpy as np

arr1 = np.arange(1, 6, 1)
arr2 = np.arange(1, 10, 2)

print(f"Soma: {arr1 + arr2}")
print(f"Subtração: {arr1 - arr2}")
print(f"Multiplicacao: {arr1 * arr2}")
print(f"Divisão: {arr1 / arr2}")
print(f"Produto escalar {np.dot(arr1, arr2)}")
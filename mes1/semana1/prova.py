import numpy as np

vendas = np.array([320, 450, 210, 580, 390, 620, 480])
print(f"Total de vendas: {vendas.sum()}")
print(f"Média: {vendas.mean()}")
print(f"Quantidade de dias acima da média: {len(vendas[vendas > vendas.mean()])}")
print(f"O Dia com mais vendas: {vendas.argmax()}")
vendas2 = vendas * 1.15
matriz = np.vstack([vendas, vendas2])
print(f"Média de vendas por dia: {matriz.mean(axis=0)}")
vendas = arr = (vendas - vendas.min()) / (vendas.max() - vendas.min())
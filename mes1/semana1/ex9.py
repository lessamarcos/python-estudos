import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

pasta = Path(__file__).parent
arr1 = np.random.randn(50)
arr2 = np.random.randn(50)
plt.scatter(arr1, arr2)
plt.title("Titulo")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.savefig(pasta / "grafico4.png")
plt.show()
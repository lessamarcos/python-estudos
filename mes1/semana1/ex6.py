import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

pasta = Path(__file__).parent

arr = np.arange(0, 10)
plt.plot(arr, arr ** 2)
plt.title("Primeiro gráfico")
plt.xlabel("Texto 1")
plt.ylabel("Texto 2")
plt.savefig(pasta / "grafico1.png")
plt.show()
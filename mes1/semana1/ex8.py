import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

pasta = Path(__file__).parent
arr = np.random.randn(1000)
plt.hist(arr, bins=20)
plt.title("Titulo")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.savefig(pasta / "grafico3.png")
plt.show()

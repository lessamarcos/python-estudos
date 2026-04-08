import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

pasta = Path(__file__).parent
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas = [4200, 3800, 5100, 4700, 5900, 5400]
plt.bar(meses, vendas)
plt.title("Vendas")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig(pasta / "grafico2.png")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

pasta = Path(__file__).parent
cidades = ["Florianópolis", "Blumenau", "Joinville", "Chapecó", "Lages"]
populacao = [516_524, 361_855, 616_066, 227_587, 156_727]
temperaturas = [22.3, 20.1, 19.8, 18.5, 15.2]

plt.bar(cidades, populacao)
plt.title("Cidades x Populacao")
plt.xlabel("Cidade")
plt.ylabel("População")
plt.savefig(pasta / "pop.png")
plt.clf()

plt.plot(cidades, temperaturas)
plt.title("Cidades x Temperaturas")
plt.xlabel("Cidade")
plt.ylabel("Temperatura")
plt.savefig(pasta / "temp.png")
plt.clf()

plt.scatter(populacao, temperaturas)
plt.title("População x Temperatura")
plt.xlabel("População")
plt.ylabel("Temperaturas")
plt.savefig(pasta / "scatter.png")



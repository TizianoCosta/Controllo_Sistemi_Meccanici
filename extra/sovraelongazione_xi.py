import numpy as np
import matplotlib.pyplot as plt

# Definizione della funzione
def M_p(xi):
    return np.exp(-xi * np.pi / np.sqrt(1 - xi**2)) * 100

# Creazione del dominio della funzione
xi = np.linspace(0, 0.99, 500)  # Evitiamo il punto 1 per non avere divisione per zero
M_p_values = M_p(xi)

# Creazione del plot in scala di grigi
plt.figure(figsize=(8, 6))
plt.plot(xi, M_p_values, color='black', label=r"$M_p = e^{-\frac{\xi \pi}{\sqrt{1-\xi^2}}} \cdot 100$")
#plt.xlabel(r"$\xi$", fontsize=14, color='black')
#plt.ylabel(r"$M_p$", fontsize=14, color='black')
#plt.title("Grafico di $M_p$ al variare di $\\xi$", fontsize=16, color='black')
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(fontsize=12, loc='upper right', frameon=False)
plt.tight_layout()

# Mostra il grafico
plt.savefig("sovraelongazione_xi.png", dpi=300)
plt.show()

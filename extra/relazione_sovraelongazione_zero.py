import numpy as np
import matplotlib.pyplot as plt

def sovraelongazione_normalizzata(alpha, xi, omega_n=1.0):
    """
    Calcola la sovraelongazione normalizzata in funzione di alpha per un sistema del secondo ordine.
    """
    # Costante di damping effettiva
    zeta_eff = alpha * xi
    # Calcolo del termine principale della sovraelongazione
    overshoot = np.exp(-np.pi * zeta_eff / np.sqrt(1 - zeta_eff**2)) if zeta_eff < 1 else 0
    return overshoot

# Parametri del sistema
omega_n = 1.0  # Frequenza naturale normalizzata
xi_values = [0.3, 0.5, 0.7, 1.4]  # Diversi valori di damping
alpha_values = np.linspace(0.1, 5, 500)  # Range di alpha

# Colori in scala di grigi
gray_colors = ['black', 'dimgray', 'gray', 'lightgray']

# Plottiamo i risultati
plt.figure(figsize=(10, 6))
for xi, color in zip(xi_values, gray_colors):
    overshoot_values = [sovraelongazione_normalizzata(alpha, xi, omega_n) for alpha in alpha_values]
    plt.plot(alpha_values, overshoot_values, label=f"$\\xi = {xi}$", color=color)

#plt.title("Sovraelongazione Normalizzata vs $\\alpha$ (Scala di Grigi)")
#plt.xlabel("$\\alpha$")
#plt.ylabel("Sovraelongazione Normalizzata")
#plt.grid(True, color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig("relazione_sovraelongazione.png", format='png', dpi=300)
plt.show()


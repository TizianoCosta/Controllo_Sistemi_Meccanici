import numpy as np
import matplotlib.pyplot as plt

# Parametri dati
s = 1e-3  # Costante s
M = 100 # Massa M
omega_n = 1000  # Pulsazione naturale omega_n
epsilon_val = [0.1, 0.3, 0.5, 0.7]  # Valore di epsilon

# Definisci l'intervallo di pulsazioni da plotare
interval = np.linspace(1.5e2/omega_n, 0.5e4/omega_n, 1000)

plt.style.use('grayscale')
plt.figure(figsize=(10, 5))

for epsilon in epsilon_val:
    # Calcola la funzione
    modulo = (s / M) * (interval)**2 / np.sqrt((1 - (interval)**2)**2 + (2 * epsilon * (interval))**2)
    # Plot
    plt.plot(interval, modulo, label=fr'xi = {epsilon}')

plt.hlines(s/M,1.5e2/omega_n, 0.5e4/omega_n, label=r's/M',color='gray', linestyle='--')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.savefig('sbilanciamento_statico.png',dpi=300)
plt.show()

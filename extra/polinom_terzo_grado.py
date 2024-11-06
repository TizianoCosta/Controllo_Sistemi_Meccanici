import numpy as np
import matplotlib.pyplot as plt

# Definisco il tempo
t = np.linspace(0, 1, 100)

# Definizione della funzione di posizione q(t)
def q(t):
    return 3 * t**2 - 2 * t**3

# Calcolo della derivata prima (velocità v(t)), seconda (accelerazione a(t)), e terza (jerk j(t)) di q(t)
def v(t):
    return 6 * t - 6 * t**2

def a(t):
    return 6 - 12 * t

def j(t):
    jerk = -12 * np.ones_like(t)  # Il jerk è costante e pari a -12 per il resto dei valori
    jerk[(t == 0) | (t == 1)] = np.nan  # Inseriamo NaN nei punti di discontinuità
    return jerk

# Creazione dei grafici
fig, axs = plt.subplots(4, 1, figsize=(8, 12), sharex=True)
#fig.suptitle("Grafici di Posizione, Velocità, Accelerazione e Jerk", fontsize=16)

# Grafico della posizione
axs[0].plot(t, q(t), color="black")
axs[0].set_ylabel("Posizione q(t)")

# Grafico della velocità
axs[1].plot(t, v(t), color="black")
axs[1].set_ylabel("Velocità v(t)")

# Grafico dell'accelerazione
axs[2].plot(t, a(t), color="black")
axs[2].set_ylabel("Accelerazione a(t)")

# Grafico del jerk
axs[3].plot(t, j(t), color="black")
axs[3].set_xlabel("Tempo t")
axs[3].set_ylabel("Jerk j(t)")

plt.subplots_adjust(hspace=0.2)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("polinom_terzo_grado.png", dpi=300)

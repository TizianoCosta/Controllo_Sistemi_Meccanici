import numpy as np
import matplotlib.pyplot as plt

# Definisco il tempo
t = np.linspace(0, 1, 100)


a4 = 35
a5 = -84
a6 = 70
a7 = -20

# Definizione della funzione di posizione q(t) per il polinomio di quinto grado
def q(t):
    return a4 * t**4 + a5 * t**5 + a6 * t**6 + a7 * t**7  # Un esempio di polinomio di quinto grado

# Calcolo della derivata prima (velocità v(t)), seconda (accelerazione a(t)), terza (jerk j(t)) e quarta (snap s(t)) di q(t)
def v(t):
    return 4*a4 * t**3 + 5*a5 * t**4 + 6*a6 * t**5 + 7*a7 * t**6

def a(t):
    return 12*a4 * t**2 + 20*a5 * t**3 + 30*a6 * t**4 + 42*a7 * t**5

def j(t):
    return 24*a4 * t + 60*a5 * t**2 + 120*a6 * t**3 + 210*a7 * t**4

# Creazione dei grafici
fig, axs = plt.subplots(4, 1, figsize=(8, 12), sharex=True)
#fig.suptitle("Grafici di Posizione, Velocità, Accelerazione, Jerk e Snap", fontsize=16)

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
axs[3].set_ylabel("Jerk j(t)")

plt.subplots_adjust(hspace=0.2)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("polinom_settimo_grado.png", dpi=300)
plt.show()

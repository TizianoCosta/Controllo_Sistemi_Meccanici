import numpy as np
import matplotlib.pyplot as plt

# Definisco il tempo
t = np.linspace(0, 1, 100)

# Definizione della funzione di posizione q(t) terzo grado
def q3(t):
    return 3 * t**2 - 2 * t**3

# Definizione della funzione di posizione q(t) per il polinomio di quinto grado
def q5(t):
    return 10 * t**3 - 15 * t**4 + 6 * t**5  # Un esempio di polinomio di quinto grado

# Definizione della funzione di posizione q(t) per il polinomio di quinto grado
def q7(t):
    return 35 * t**4 - 84 * t**5 + 70 * t**6 - 20 * t**7  # Un esempio di polinomio di quinto grado


# Creazione dei grafici
plt.plot(t,q3(t), label="Grado 3")
plt.plot(t,q5(t), label="Grado 5")
plt.plot(t,q7(t), label="Grado 7")
plt.legend()
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("confronto_polin.png", dpi=300)
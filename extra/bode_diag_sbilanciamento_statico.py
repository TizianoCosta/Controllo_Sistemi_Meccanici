import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Definire la funzione di trasferimento
def transfer_function(w, s, M, omega_n, epsilon):
    # Calcolare il termine del modulo
    num = (w / omega_n) ** 2
    denom = np.sqrt((1 - (w / omega_n) ** 2) ** 2 + (2 * epsilon * w / omega_n) ** 2)
    
    # Funzione di trasferimento
    H = (w * s / M) * num / denom
    return H

# Parametri della funzione di trasferimento
M = 100  # Massa (esempio, da definire)
s = 1e-3
omega_n = 1e3  # Frequenza naturale (esempio, da definire)
epsilon = 0.8  # Damping (esempio, da definire)

# Definire l'intervallo di frequenze
omega = np.logspace(2, 5, 1000)  # Frequenze logaritmiche

# Calcolare il modulo e la fase della funzione di trasferimento
H = transfer_function(omega, s, M, omega_n, epsilon)
magnitude = np.abs(H)  # Modulo

# Modulo
plt.figure(figsize=(8, 6))
plt.semilogx(omega, 20 * np.log10(magnitude), color='black')  # Modulo in dB (bianco e nero)
#plt.title('Bode Plot - Magnitude', fontsize=14, color='black')
#plt.xlabel('Frequency [rad/s]', fontsize=12, color='black')
#plt.ylabel('Magnitude [dB]', fontsize=12, color='black')
plt.grid(True, which='both', axis='both', color='gray', linestyle='--')
plt.tick_params(axis='both', labelsize=10, colors='black')
plt.gca().set_facecolor('white')
    
plt.tight_layout()
plt.savefig('sbilanciamento_statico.png',dpi=300)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parametri del sistema (esempio con doppio zero e doppio polo)
omega_n = 100  # Frequenza naturale del numeratore (rad/s)
zeta = 0.1     # Fattore di smorzamento numeratore

omega_p = 150  # Frequenza naturale del denominatore (rad/s)
zeta_p = 0.3   # Fattore di smorzamento denominatore

# Numeratore (doppio zero)
numeratore = [1, 2 * zeta * omega_n, omega_n**2]

# Denominatore (doppio polo)
denominatore = [1, 2 * zeta_p * omega_p, omega_p**2]

# Creazione della funzione di trasferimento
system = signal.TransferFunction(numeratore, denominatore)

# Frequenze per la simulazione
frequenze = np.logspace(0, 3, 1000)  # Frequenze da 1Hz a 1000Hz
omega = 2 * np.pi * frequenze

# Risposta in frequenza
w, mag, phase = signal.bode(system, omega)

# Plot del modulo
plt.figure(figsize=(12, 6))

# Subplot per il modulo
plt.subplot(2, 1, 1)
plt.semilogx(frequenze, mag, label="Modulo |H(ω)|")
#plt.title("Risposta in frequenza di un sistema con doppio zero e doppio polo (Modulo e Fase)")
#plt.xlabel("Frequenza [Hz]")
#plt.ylabel("Modulo |H(ω)| [dB]")
plt.grid(True, which="both", ls="--")
plt.axvline(x=omega_n/(2*np.pi), color='grey', linestyle='--', label=f"Anti-Risonanza a {omega_n/(2*np.pi):.2f} Hz")
plt.legend()

# Subplot per la fase
plt.subplot(2, 1, 2)
plt.semilogx(frequenze, phase, label="Fase ∠H(ω)")
#plt.xlabel("Frequenza [Hz]")
#plt.ylabel("Fase [gradi]")
plt.grid(True, which="both", ls="--")
plt.legend()

# Mostra il grafico
plt.tight_layout()
plt.savefig('esempio_antirisonanza.png',dpi=300)
plt.show()

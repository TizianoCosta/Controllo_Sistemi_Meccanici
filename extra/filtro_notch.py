import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqresp, TransferFunction

# Definizione dei parametri
xi_p_values = [0.05, 0.1, 0.3, 0.5]  # Smorzamenti al denominatore
omega_0 = 1.0  # Frequenza centrale (rad/s)

# Definizione della frequenza
w = np.logspace(-1, 1, 250)  # Frequenze da 0.1 a 100 rad/s

plt.style.use('grayscale')
plt.figure(figsize=(12, 8))

# Plot dell'ampiezza
plt.subplot(2, 1, 1)
for xi_p in xi_p_values:
    xi_d = xi_p * 4
    # Numeratore e denominatore del filtro notch
    num = [1, 2 * xi_p * omega_0, omega_0**2]
    den = [1, 2 * xi_d * omega_0, omega_0**2]

    # Creazione della funzione di trasferimento
    system = TransferFunction(num, den)

    # Calcolo della risposta in frequenza
    _, H = freqresp(system, w)

    # Modulo in dB
    H_dB = 20 * np.log10(abs(H))

    # Plot della risposta in frequenza
    plt.plot(w, H_dB, label=f"$\\xi_p={xi_p}$")

plt.xscale('log')
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Plot della fase
plt.subplot(2, 1, 2)
for xi_p in xi_p_values:
    xi_d = xi_p * 4
    # Numeratore e denominatore del filtro notch
    num = [1, 2 * xi_p * omega_0, omega_0**2]
    den = [1, 2 * xi_d * omega_0, omega_0**2]

    # Creazione della funzione di trasferimento
    system = TransferFunction(num, den)

    # Calcolo della risposta in frequenza
    _, H = freqresp(system, w)

    # Fase in gradi
    phase = np.angle(H, deg=True)

    # Plot della risposta in fase
    plt.plot(w, phase, label=f"$\\xi_p={xi_p}$")

plt.xscale('log')
plt.grid(which='both', linestyle='--', linewidth=0.5)
plt.legend()

plt.tight_layout()
plt.savefig('filtro_notch_xip_su_xid_costante.png',dpi=300)
plt.show()
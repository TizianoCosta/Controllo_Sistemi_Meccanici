import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Parametri del sistema
A0 = 1.0      # Ampiezza iniziale
delta = 0.05  # Decremento logaritmico
omega0 = 10   # Pulsazione naturale (rad/s)
t_max = 10    # Tempo massimo (secondi)
num_points = 1000  # Numero di punti da considerare per il grafico

# Calcolare la pulsazione smorzata
omega_d = omega0 * np.sqrt(1 - (delta / omega0)**2)  # Pulsazione smorzata

# Creare il tempo e calcolare l'ampiezza smorzata
t_values = np.linspace(0, t_max, num_points)
A_values = A0 * np.exp(-delta * t_values) * np.cos(omega_d * t_values)

# Trova i picchi dell'oscillazione (massimi locali)
peaks, _ = find_peaks(A_values)

# Calcolare il decremento logaritmico tra i picchi
peak_amplitudes = A_values[peaks]
if len(peak_amplitudes) > 1:
    # Calcolare il decremento logaritmico tra il primo e il secondo picco
    delta_calculated = 0.5 * np.log(peak_amplitudes[0] / peak_amplitudes[1])
else:
    delta_calculated = None

# Calcolare la frazione di smorzamento xi
if delta_calculated is not None:
    xi = delta_calculated / np.sqrt(4 * np.pi**2 + delta_calculated**2)
else:
    xi = None

# Calcolare la pulsazione naturale omega_n
if xi is not None:
    omega_n = omega_d / np.sqrt(1 - xi**2)
else:
    omega_n = None

# Creare il grafico
plt.figure(figsize=(10, 6))
plt.plot(t_values, A_values, label="Oscillazione smorzata")
plt.scatter(t_values[peaks], peak_amplitudes, color='red', label="Picchi")
plt.title(f"Oscillazione smorzata con decremento logaritmico\n"
          f"Decremento logaritmico (calcolato): {delta_calculated:.4f}\n"
          f"Frazione di smorzamento xi: {xi:.4f}\n"
          f"Pulsazione naturale omega_n: {omega_n:.2f} rad/s")
#plt.xlabel("Tempo (s)")
#plt.ylabel("Ampiezza")
plt.grid(True)
plt.legend()

# Mostrare il grafico
plt.savefig('es_decremento_log.png',dpi=300)
plt.show()

# Output dei picchi trovati, decremento logaritmico, smorzamento e pulsazione naturale
print("Picchi trovati (tempi e ampiezze):")
for peak, amp in zip(t_values[peaks], peak_amplitudes):
    print(f"Tempo: {peak:.2f} s, Ampiezza: {amp:.4f}")

if delta_calculated is not None:
    print(f"\nDecremento logaritmico calcolato: {delta_calculated:.4f}")
    print(f"Frazione di smorzamento xi calcolata: {xi:.4f}")
    print(f"Pulsazione naturale omega_n calcolata: {omega_n:.2f} rad/s")

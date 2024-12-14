import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import math

# Parametri della funzione di trasferimento
rho = 1
omega_z = 1e2  # Frequenza naturale dei poli
xi_z = 0.05       # Coefficiente di smorzamento dei poli
omega_p = omega_z * math.sqrt(1 + rho)  # Frequenza naturale degli zeri
xi_p = xi_z * math.sqrt(1 + rho)        # Coefficiente di smorzamento degli zeri

K_pv = 10
K_T = 10
T_i = 1 / 10
omega_tv = 1e3
omega_I = 3e3

# Variabile di Laplace
s = ctrl.TransferFunction.s

# Definizione di Gvm
numerator_g = (s**2 / omega_z**2 + s * 2 * xi_z / omega_z + 1)
denominator_g = s * (s**2 / omega_p**2 + s * 2 * xi_p / omega_p + 1)
Gvm = numerator_g / denominator_g

# Definizione di Cv, H_tv e W_i
Cv = (1 + s * T_i) / s / T_i
H_tv = 1 / (s / omega_tv + 1)**2
W_i = 1 / (s / omega_I + 1)

# Definizione di L_v
L_v = Gvm * K_T * Cv * H_tv * W_i * K_pv

# Frequenze per il Bode plot
omega = np.logspace(1, 3.5, 500)  # Da 10^1 a 10^6 rad/s

# Calcolo del guadagno
mag_Gvm_KT, _, _ = ctrl.bode(Gvm * K_T * K_pv, omega, Plot=False)
mag_Lv, _, _ = ctrl.bode(L_v, omega, Plot=False)

# Plot in bianco e nero
plt.figure(figsize=(8, 6))
plt.semilogx(omega, 20 * np.log10(mag_Gvm_KT), label='$|G_{vm} \cdot K_T \cdot K_{pv}|$', color='black')
plt.semilogx(omega, 20 * np.log10(mag_Lv), label='$|L_v|$', color='grey')

# Configurazioni del grafico
plt.grid(which='both', linestyle='--', linewidth=0.5, color='gray')
plt.legend(fontsize=12)
plt.tight_layout()

# Mostra il plot
plt.savefig('risonanza_bassa_f_Gvm_vs_Lv.png')
plt.show()
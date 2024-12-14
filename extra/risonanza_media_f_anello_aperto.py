import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import math

# Parametri della funzione di trasferimento
rho = 1
omega_z = 1e3  # Frequenza naturale dei poli
xi_z = 0.05       # Coefficiente di smorzamento dei poli
omega_p = 1400  # Frequenza naturale degli zeri
xi_p = xi_z * math.sqrt(1 + rho)        # Coefficiente di smorzamento degli zeri

K_pv = 100
K_T = 10
T_i = 1 / 10
omega_tv = 1.2e3
omega_I = 1.5e3

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
omega = np.logspace(2, 4, 500)  # Da 10^1 a 10^6 rad/s

# Calcolo del guadagno
mag_Gvm_KT, phase_Gvm_KT, _ = ctrl.bode(Gvm * K_T * K_pv, omega, Plot=False)
mag_Lv, phase_Lv, _ = ctrl.bode(L_v, omega, Plot=False)

# Plot in bianco e nero
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# Modulo
axs[0].semilogx(omega, 20 * np.log10(mag_Gvm_KT), label='$|G_{vm} \\cdot K_T \\cdot K_{pv}|$', color='black')
axs[0].semilogx(omega, 20 * np.log10(mag_Lv), label='$|L_v|$', color='grey')
axs[0].grid(which='both', linestyle='--', linewidth=0.5, color='gray')
axs[0].legend(fontsize=12)

# Fase
axs[1].semilogx(omega, phase_Gvm_KT * (180 / np.pi), label='$\\angle G_{vm} \\cdot K_T \\cdot K_{pv}$', color='black')
axs[1].semilogx(omega, phase_Lv * (180 / np.pi), label='$\\angle L_v$', color='grey')
axs[1].grid(which='both', linestyle='--', linewidth=0.5, color='gray')
axs[1].legend(fontsize=12)

# Configurazioni finali
plt.tight_layout()
plt.savefig('risonanza_media_f_Gvm_vs_Lv.png')
plt.show()
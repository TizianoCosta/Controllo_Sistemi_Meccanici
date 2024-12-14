import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
import math

# Parametri della funzione di trasferimento
rho = 4
omega_z = 1e2  # Frequenza naturale dei poli
xi_z = 0.7       # Coefficiente di smorzamento dei poli
omega_p = omega_z * math.sqrt(1 + rho)  # Frequenza naturale degli zeri
xi_p = xi_z * math.sqrt(1 + rho)        # Coefficiente di smorzamento degli zeri

#K_pv = 10 #Kp2
K_pv = 55 #Kp3
K_T = 10
T_i = 1 / 10
omega_tv = 1e3
omega_I = 3e3

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

Wm = L_v / (1 + L_v)

numerator_T = (s * 2 * xi_z / omega_z + 1)
denominator_T = (s**2 / omega_z**2 + s * 2 * xi_z / omega_z + 1)
T = numerator_T / denominator_T

Wc = Wm * T

# Risposta al gradino
time = np.linspace(0, 0.4, 1000)  # Intervallo di tempo
t_out, y_Wm = ctrl.step_response(Wm, time)
_, y_Wc = ctrl.step_response(Wc, time)

# Visualizzazione dei risultati
plt.figure(figsize=(10, 6))

plt.plot(t_out, y_Wm, label="Risposta al gradino di Wc", color='grey')
plt.plot(t_out, y_Wc, label="Risposta al gradino di Wm", color='black')


plt.legend(fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig('step_response_Kp3.png',dpi=300)
plt.show()

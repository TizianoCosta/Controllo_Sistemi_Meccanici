import numpy as np
import math
import matplotlib.pyplot as plt
import control as ctrl

# Parametri della funzione di trasferimento
K = 1e-4 #Nm/rd
D = 5e-8 #Nms/rd
tauV = 40e-3 / (2*math.pi)
tauR = 1/10
Jc = 100 * tauV**2 / 0.95 # considero un carico traslante di 100kg
Jm = 0.6e-4
Jtot = Jm + Jc * tauR**2 / 0.95
#rho = tauR**2 * Jc / Jm
rho = 0.5
#omega_z = math.sqrt(K * Jtot / Jc / Jm)  # Frequenza naturale dei poli
omega_z = 100
#xi_z = D / (2 * math.sqrt(Jc * K))  # Coefficiente di smorzamento dei poli
xi_z = 0.1
omega_p = omega_z * math.sqrt(1 + rho)  # Frequenza naturale degli zeri
xi_p = xi_z * math.sqrt(1 + rho)  # Coefficiente di smorzamento degli zeri

T_i = 4 * xi_p**2 / omega_p
Kp = 1
KT = 1e-1

s = ctrl.TransferFunction.s
numerator_T = tauR * (s * 2 * xi_z / omega_z + 1)
denominator_T = Jtot * (s**2 / omega_z**2 + s * 2 * xi_z / omega_z + 1)
T = numerator_T / denominator_T

numerator_G = (s**2 / omega_z**2 + s * 2 * xi_z / omega_z + 1)
denominator_G = Jtot * s * (s**2 / omega_p**2 + s * 2 * xi_p / omega_p + 1)
Gvm = numerator_G / denominator_G

numerator_PI = (1 + s * T_i) * Kp
denominator_PI = s
PI = numerator_PI / denominator_PI

Wv = Gvm * PI * KT / (1 + Gvm * PI * KT)

Load = Wv * T

# Calcolare il modulo per entrambe le funzioni di trasferimento
omega = np.logspace(1.9, 2.4, 500)  # Definizione delle frequenze
mag_Load, _, _ = ctrl.bode(Load, omega, Plot=False)
mag_Wv, _, _ = ctrl.bode(Wv, omega, Plot=False)
mag_T, _, _ = ctrl.bode(T, omega, Plot=False)

# Grafico del modulo
plt.style.use('grayscale')
plt.figure()
plt.semilogx(omega, 20 * np.log10(mag_Load), label="|Load| (dB)")
plt.semilogx(omega, 20 * np.log10(mag_Wv), label="|Wv| (dB)")
plt.semilogx(omega, 20 * np.log10(mag_T), label="|T| (dB)")

# Aggiungere linee tratteggiate per omega_z e omega_p
plt.axvline(x=omega_z, color='black', linestyle='--', label='$\omega_z$')
plt.axvline(x=omega_p, color='grey', linestyle='--', label='$\omega_p$')


# Aggiungere etichette e legenda
plt.legend()

# Mostrare il grafico
plt.savefig('colocato_v_lato_carico.png',dpi=300)
plt.show()
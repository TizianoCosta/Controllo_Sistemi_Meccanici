import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
import math

# Parametri del sistema
K = 1e-4  # Nm/rd
D = 5e-8  # Nms/rd
tauV = 40e-3 / (2 * math.pi)
tauR = 1 / 10
Jc = 100 * tauV**2 / 0.95  # carico traslante di 100kg
Jm = 0.6e-4
Jtot = Jm + Jc * tauR**2 / 0.95
#rho = tauR**2 * Jc / Jm
rho = 1
#omega_z = math.sqrt(K * Jtot / Jc / Jm)  # Frequenza naturale dei poli
omega_z = 10
#xi_z = D / (2 * math.sqrt(Jc * K))  # Coefficiente di smorzamento dei poli
xi_z = 0.1
omega_p = omega_z * math.sqrt(1 + rho)  # Frequenza naturale degli zeri
xi_p = xi_z * math.sqrt(1 + rho)  # Coefficiente di smorzamento degli zeri

s = ctrl.TransferFunction.s
numerator = (s**2 / omega_z**2 + s * 2 * xi_z / omega_z + 1)
denominator = Jtot * s * (s**2 / omega_p**2 + s * 2 * xi_p / omega_p + 1)
H = numerator / denominator

# Scalo H per includere K
H_with_K = H * ctrl.TransferFunction([1], [1])  # Placeholder per K

# Gamma di valori di K
K_values = np.linspace(0, 0.001, 500)  # Adatta la gamma in base alla scala del tuo sistema

# Luogo delle radici
plt.style.use('grayscale')
plt.figure()
ctrl.root_locus(H_with_K, kvect=K_values, grid=False)
plt.ylim(-20, 20)
plt.xlim(-10,1)
plt.savefig('controllo_v_colocato.png', dpi=300)
plt.show()
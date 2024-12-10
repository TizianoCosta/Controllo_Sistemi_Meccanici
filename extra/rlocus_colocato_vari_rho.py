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

# Valori di rho da considerare
rho_values = [0.2, 1, 2]

# Configurazione dei subplot
fig, axs = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)
plt.style.use('grayscale')

for i, rho in enumerate(rho_values):
    # Calcolo parametri basati su rho
    omega_z = 10  # Frequenza naturale dei poli (esempio fisso)
    xi_z = 0.1  # Coefficiente di smorzamento dei poli (esempio fisso)
    omega_p = omega_z * math.sqrt(1 + rho)  # Frequenza naturale degli zeri
    xi_p = xi_z * math.sqrt(1 + rho)  # Coefficiente di smorzamento degli zeri
    
    # Funzione di trasferimento
    s = ctrl.TransferFunction.s
    numerator = (s**2 / omega_z**2 + s * 2 * xi_z / omega_z + 1)
    denominator = Jtot * s * (s**2 / omega_p**2 + s * 2 * xi_p / omega_p + 1)
    H = numerator / denominator

    # Scalo H per includere K
    H_with_K = H * ctrl.TransferFunction([1], [1])  # Placeholder per K

    # Gamma di valori di K
    K_values = np.linspace(0, 0.001, 500)  # Adatta la gamma in base alla scala del tuo sistema

    # Luogo delle radici
    rlocus_data = ctrl.root_locus(H_with_K, kvect=K_values, plot=False)
    
    # Tracciamento del luogo delle radici sul subplot corrente
    axs[i].plot(rlocus_data[0].real, rlocus_data[0].imag)
    axs[i].set_title(f'Luogo delle radici (ρ = {rho})')
    axs[i].set_xlabel('Re')
    axs[i].set_ylabel('Im')
    axs[i].grid(True)

# Limiti comuni per i grafici
for ax in axs:
    ax.set_xlim(-10, 1)
    ax.set_ylim(-20, 20)

# Salvataggio e visualizzazione
plt.savefig('controllo_v_colocato_subplot_rho.png', dpi=300)
plt.show()

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

def grafico_zeri_poli(omega_p, xi_p, omega_z, xi_z):
    """
    Genera un grafico di zeri e poli in piano complesso per una funzione di trasferimento
    e visualizza la pulsazione (omega) e la proiezione sull'asse reale (-xi*omega) sia per poli che per zeri.
    
    :param omega_p: Frequenza naturale dei poli (ω_p)
    :param xi_p: Coefficiente di smorzamento dei poli (ξ_p)
    :param omega_z: Frequenza naturale degli zeri (ω_z)
    :param xi_z: Coefficiente di smorzamento degli zeri (ξ_z)
    """
    # Definizione del numeratore e denominatore in forma canonica
    numeratore = [1 / omega_z**2, 2 * xi_z / omega_z, 1]
    denominatore = [1 / omega_p**2, 2 * xi_p / omega_p, 1]

    # Calcola zeri e poli
    zeri, poli, _ = tf2zpk(numeratore, denominatore)

    # Crea il grafico
    plt.figure(figsize=(8, 8))
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='--')

    # Disegna poli
    for p in poli:
        # Segmento dall'origine al polo
        plt.plot([0, np.real(p)], [0, np.imag(p)], 'g--', label=r'Pulsazione $\omega_p$' if p == poli[0] else "")
        # Proiezione sull'asse reale
        plt.plot([np.real(p), np.real(p)], [0, np.imag(p)], 'orange', linestyle='--', label=r'Proiezione $-\xi_p \omega_p$' if p == poli[0] else "")
        # Annotazioni
        plt.text(np.real(p) / 2, np.imag(p) / 2, r'$\omega_p$', color='green', fontsize=12)
        plt.text(np.real(p) - 0.05, 0.01, r'$-\xi_p \omega_p$', color='orange', fontsize=12)

    # Disegna zeri
    for z in zeri:
        # Segmento dall'origine allo zero
        plt.plot([0, np.real(z)], [0, np.imag(z)], 'b--', label=r'Pulsazione $\omega_z$' if z == zeri[0] else "")
        # Proiezione sull'asse reale
        plt.plot([np.real(z), np.real(z)], [0, np.imag(z)], 'purple', linestyle='--', label=r'Proiezione $-\xi_z \omega_z$' if z == zeri[0] else "")
        # Annotazioni
        plt.text(np.real(z) / 2, np.imag(z) / 2, r'$\omega_z$', color='blue', fontsize=12)
        plt.text(np.real(z) - 0.05, 0.01, r'$-\xi_z \omega_z$', color='purple', fontsize=12)

    # Personalizzazione del grafico
    plt.scatter(np.real(zeri), np.imag(zeri), marker='o', color='red', label='Zeri')
    plt.scatter(np.real(poli), np.imag(poli), marker='x', color='blue', label='Poli')

    # Limiti statici
    plt.ylim(-10, 10)  # Imposta il range dell'asse immaginario

    #plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    #plt.xlabel("Reale")
    #plt.ylabel("Immaginario")
    #plt.title("Zeri e Poli nel piano complesso con annotazioni")
    plt.axis('equal')
    plt.savefig('poli_zeri_Gvm.png', dpi=300)
    plt.show()

# Parametri della funzione di trasferimento
K = 1e-4 #Nm/rd
D = 5e-4 #Nms/rd
tauV = 40e-3 / (2*math.pi)
tauR = 1/10
Jc = 100 * tauV**2 / 0.95 # considero un carico traslante di 100kg
Jm = 0.6e-4
Jtot = Jm + Jc * tauR**2 / 0.95
rho = tauR**2 * Jc / Jm
omega_z = math.sqrt(K*Jtot/Jc/Jm)  # Frequenza naturale dei poli
xi_z = D / (2 * math.sqrt(Jc * K))     # Coefficiente di smorzamento dei poli
omega_p = omega_z * math.sqrt(1+rho)  # Frequenza naturale degli zeri
xi_p = xi_z * math.sqrt(1+rho)     # Coefficiente di smorzamento degli zeri

# Genera il grafico
grafico_zeri_poli(omega_p, xi_p, omega_z, xi_z)

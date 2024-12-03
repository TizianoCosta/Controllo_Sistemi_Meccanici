import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode
from sympy import symbols, expand, simplify, Poly

# Definizione della variabile simbolica
s = symbols('s')

# Parametri del sistema
mecc = 1  # Costante di tempo del polo meccanico
zeroPI = 10  # Costante di tempo dello zero del PI
trasduttore = 1e3  # Costante di tempo del polo del trasduttore
anelloI = 2e3 # Costante di tempo del polo dell'anello di corrente

# Definizione della funzione di trasferimento parametrizzata
numerator = (zeroPI + s) * 1e6
denominator = s * (mecc + s) * (trasduttore + s) * (anelloI + s)
transfer_function = numerator / denominator

# Espansione dei polinomi e calcolo dei coefficienti
num_poly = Poly(simplify(expand(numerator)), s).all_coeffs()
den_poly = Poly(simplify(expand(denominator)), s).all_coeffs()

# Conversione dei coefficienti da SymPy a float
num_coeffs = [float(c) for c in num_poly]
den_coeffs = [float(c) for c in den_poly]

# Coefficienti moltiplicativi per variare il sistema
multipliers = [50, 160, 500]

# Grafico in bianco e nero
plt.style.use('grayscale')

# Creazione delle figure
fig, (ax_mag, ax_phase) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Funzione per calcolare il margine di fase
def calculate_phase_margin(w, mag, phase):
    # Trova l'indice della pulsazione di attraversamento (|H(jw)| = 1)
    idx = np.argmin(np.abs(mag - 0))  # Poiché il modulo è in dB
    w_cross = w[idx]  # Pulsazione di attraversamento
    phase_at_cross = phase[idx]  # Fase corrispondente
    phase_margin = 180 + phase_at_cross  # Margine di fase
    return w_cross, phase_at_cross, phase_margin

# Ciclo sui moltiplicatori
for k in multipliers:
    # Modifica del numeratore moltiplicando per k
    num_k = [coeff * k for coeff in num_coeffs]

    # Creazione della funzione di trasferimento
    system = TransferFunction(num_k, den_coeffs)

    # Calcolo del bode plot
    w, mag, phase = bode(system)

    # Calcolo del margine di fase
    w_cross, phase_at_cross, phase_margin = calculate_phase_margin(w, mag, phase)

    # Plot del modulo
    ax_mag.plot(w, mag, label=f'J={1/k}, w_cross={w_cross:.2f} rad/s')

    # Evidenziazione della pulsazione di attraversamento
    ax_mag.axvline(w_cross, color='gray', linestyle='--', linewidth=0.8)

    # Plot della fase
    ax_phase.plot(w, phase, label=f'J={1/k}, Phase Margin={phase_margin:.1f}°')

    # Evidenziazione del margine di fase
    ax_phase.scatter([w_cross], [phase_at_cross], color='black', zorder=5)
    ax_phase.axhline(phase_at_cross, color='gray', linestyle='--', linewidth=0.8)

# Configurazione del grafico del modulo
#ax_mag.set_title('Modulo della funzione di trasferimento')
#ax_mag.set_ylabel('Modulo [dB]')
ax_mag.set_xscale('log')
ax_mag.legend()
#ax_mag.grid(which='both', linestyle='--', linewidth=0.5)

# Configurazione del grafico della fase
#ax_phase.set_title('Fase della funzione di trasferimento')
#ax_phase.set_ylabel('Fase [°]')
#ax_phase.set_xlabel('Pulsazione [rad/s]')
ax_phase.set_xscale('log')
ax_phase.legend()
#ax_phase.grid(which='both', linestyle='--', linewidth=0.5)

# Mostra i grafici
plt.tight_layout()
plt.savefig("anello_velocita_J_variabile.png", dpi=300)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Parametri del sistema
xi = 0.5  # Smorzamento
omega_n = 1  # Frequenza naturale
alphas = [1, 2, 4, 100]  # Valori di alpha

def transfer_function(alpha, xi, omega_n):
    """
    Crea la funzione di trasferimento del sistema del secondo ordine
    """
    # Coefficienti del numeratore e denominatore
    num = [1, alpha * xi * omega_n]
    den = [1, 2 * xi * omega_n, omega_n**2]
    return lti(num, den)

def plot_normalized_responses(alphas, xi, omega_n, filename="normalized_response.png"):
    """
    Traccia i grafici normalizzati rispetto al valore finale per valutare
    la sovraelongazione percentuale.
    """
    t = np.linspace(0, 10, 1000)  # Intervallo di tempo normale
    linestyles = ['-', '--', '-.', ':']  # Stili di linea per distinguere i grafici
    
    plt.figure(figsize=(10, 6))
    for alpha, linestyle in zip(alphas, linestyles):
        system = transfer_function(alpha, xi, omega_n)
        t_out, response = step(system, T=t)  # Calcola la risposta al gradino
        
        # Normalizzazione rispetto al valore finale
        final_value = response[-1]  # Assumiamo che l'ultimo valore sia il valore finale
        response_normalized = response / final_value
        
        # Calcolo della sovraelongazione percentuale
        overshoot = (np.max(response_normalized) - 1) * 100
        
        plt.plot(omega_n * t_out, response_normalized, linestyle, color="black", 
                 label=f"$\\alpha={alpha}, \\; OS={overshoot:.1f}\\%$")
    
    #plt.title("Risposta normalizzata al gradino per diversi valori di $\\alpha$")
    #plt.xlabel("$\\omega_n t$")  # Asse delle ascisse scalato
    #plt.ylabel("Risposta normalizzata")
    #plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    
    # Salva il grafico come PNG
    plt.savefig(filename, format='png', dpi=300)  # Alta qualità (300 DPI)
    plt.show()

# Esegui il grafico e salva come PNG
plot_normalized_responses(alphas, xi, omega_n, filename="influenza_zero_su_sovraelong.png")

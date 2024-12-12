import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.signal import lti, lsim

# Parametri del sistema
rho = 0.1
J = 1
omega_z = 100  # Frequenza naturale del sistema (rad/s)
omega_p = omega_z * math.sqrt(1+rho)
xi_z = 0.01   # Fattore di smorzamento (sotto-smorzato per risonanza)
xi_p = xi_z * math.sqrt(1+rho)

def generate_trajectory_sinusoidale(T_max, dt, T_fermo):
    A = 2*math.pi*(1/T_max)**2   # Ampiezza dell'accelerazione sinusoidale
    t = np.arange(0, T_max, dt)  # Tempo di movimento fino a T_max
    
    # Accelerazione sinusoidale che parte da 0 e ritorna a 0
    accelerazione = A * np.sin(2*math.pi/T_max * t)  # Partenza da 0, oscilla e torna a 0
    
    # Integrare per ottenere la velocità (v = ∫a dt)
    velocita = np.cumsum(accelerazione) * dt
    
    # Integrare per ottenere la posizione (p = ∫v dt)
    posizione = np.cumsum(velocita) * dt
    
    # Posizione, velocità e accelerazione per il periodo di fermo
    t_fermo = np.arange(T_max, T_max + T_fermo, dt)
    posizione_fermo = np.ones_like(t_fermo)
    velocita_fermo = np.zeros_like(t_fermo)
    accelerazione_fermo = np.zeros_like(t_fermo)
    
    # Estensione temporale solo per le variabili, non per il tempo
    t_tot = np.concatenate([t, t_fermo])
    posizione_tot = np.concatenate([posizione, posizione_fermo])
    velocita_tot = np.concatenate([velocita, velocita_fermo])
    accelerazione_tot = np.concatenate([accelerazione, accelerazione_fermo])
    
    return t_tot, posizione_tot, velocita_tot, accelerazione_tot

# Creazione del sistema del secondo ordine
num = [1 / omega_z**2, 2 * xi_z / omega_z, 1]
den = [J / omega_p**2, J * 2 * xi_p / omega_p, J, 0]
sistema = lti(num, den)

# Sistema per l'errore di posizione
num_errore = [1 / omega_z**2]
den_errore = [1 / omega_z**2, 2 * xi_z / omega_z, 1]
sistema_errore = lti(num_errore, den_errore)

# Parametri di simulazione
T_max = 5
dt = 0.01
T_fermo = 2  # Durata del periodo di fermo (tempo in cui la posizione è ferma a 1)

# Generazione delle traiettorie
t_tot, posizione_tot, velocita_tot, accelerazione_tot = generate_trajectory_sinusoidale(T_max, dt, T_fermo)

# Simulazione della risposta del sistema
t_out, y_out, _ = lsim(sistema, U=accelerazione_tot, T=t_tot)

# Calcolo dell'errore di posizione
t_out, errore, _ = lsim(sistema_errore, U=accelerazione_tot, T=t_tot)

# Tracciamento dei risultati
plt.style.use('grayscale')
plt.figure(figsize=(10, 8))

# Posizione
plt.subplot(4, 1, 1)
plt.plot(t_tot, posizione_tot, label='Posizione')
plt.title('Posizione')
plt.legend()

# Velocità
plt.subplot(4, 1, 2)
plt.plot(t_tot, velocita_tot, label='Velocità')
plt.title('Velocità')
plt.legend()

# Accelerazione
plt.subplot(4, 1, 3)
plt.plot(t_tot, accelerazione_tot, label='Accelerazione')
plt.title('Accelerazione')
plt.legend()

# Errore di posizione
plt.subplot(4, 1, 4)
plt.plot(t_out, errore, label='Errore di posizione')
plt.title('Errore di posizione')
plt.legend()

plt.tight_layout()
plt.savefig('sinusoidale_colocato_v.png', dpi=300)
plt.show()

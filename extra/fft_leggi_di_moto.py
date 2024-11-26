import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
freq_max = 5
def polinomiale_terzo_grado(t, T):
    """Legge di moto polinomiale di terzo grado"""
    return 3 * (t / T)**2 - 2 * (t / T)**3

def polinomiale_quinto_grado(t, T):
    """Legge di moto polinomiale di quinto grado"""
    return 10 * (t / T)**3 - 15 * (t / T)**4 + 6 * (t / T)**5

def armonica_modificata(t, T):
    """Legge di moto armonica modificata con discontinuità"""
    if t < T / 2:
        return 0.5 * (1 - np.cos(2 * np.pi * t / T))
    else:
        return 0.5 * (1 - np.cos(np.pi))  # Mantiene continuità della posizione

def cicloidale_corretta(t, T):
    """Legge di moto cicloidale corretta"""
    return (t / T) - (1 / (2 * np.pi)) * np.sin(2 * np.pi * t / T)

def compute_fourier_acceleration(law_func, T, N=1000, max_freq=100):
    """Calcola i contenuti armonici dell'accelerazione e filtra per frequenze fino a max_freq."""
    t = np.linspace(0, T, N)
    dt = t[1] - t[0]
    
    # Calcolo della posizione e accelerazione
    pos = np.array([law_func(tt, T) for tt in t])
    acc = np.gradient(np.gradient(pos, dt), dt)  # Derivata seconda

    # Trasformata di Fourier
    acc_fft = fft(acc)
    freq = fftfreq(N, dt)

    # Considera solo il semispettro positivo e filtra per frequenze <= max_freq
    mask = (freq > 0) & (freq <= max_freq)
    harmonics = np.abs(acc_fft[mask])
    harmonics /= harmonics.max()  # Normalizzazione
    return freq[mask], harmonics

def plot_harmonics_separate():
    """Plot separati dei contenuti armonici di accelerazione, limitati a 10 Hz."""
    T = 10  # Durata totale del moto

    # Configura i plot
    plt.figure(figsize=(10, 6))

    # Primo grafico: Polinomiali
    plt.subplot(2, 1, 1)
    freq, harmonics = compute_fourier_acceleration(polinomiale_terzo_grado, T, max_freq=freq_max)
    plt.plot(freq, harmonics, label="Polinomiale 3° grado", color="black", linestyle="solid")
    freq, harmonics = compute_fourier_acceleration(polinomiale_quinto_grado, T, max_freq=freq_max)
    plt.plot(freq, harmonics, label="Polinomiale 5° grado", color="black", linestyle="dashed")
    #plt.title("Polinomiali: Contenuti armonici di accelerazione (fino a 10 Hz)")
    #plt.xlabel("Frequenza (Hz)")
    #plt.ylabel("Ampiezza normalizzata")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    # Secondo grafico: Armonica e Cicloidale
    plt.subplot(2, 1, 2)
    freq, harmonics = compute_fourier_acceleration(armonica_modificata, T, max_freq=freq_max)
    plt.plot(freq, harmonics, label="Armonica", color="gray", linestyle="solid")
    freq, harmonics = compute_fourier_acceleration(cicloidale_corretta, T, max_freq=freq_max)
    plt.plot(freq, harmonics, label="Cicloidale", color="gray", linestyle="dashed")
    #plt.title("Armonica e Cicloidale: Contenuti armonici di accelerazione (fino a 10 Hz)")
    #plt.xlabel("Frequenza (Hz)")
    #plt.ylabel("Ampiezza normalizzata")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    # Salva i grafici
    plt.tight_layout()
    filename = "fft_leggi_di_moto.png"
    plt.savefig(filename, dpi=300)
    plt.show()

if __name__ == "__main__":
    plot_harmonics_separate()
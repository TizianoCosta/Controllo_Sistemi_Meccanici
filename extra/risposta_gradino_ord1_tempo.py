import numpy as np
import matplotlib.pyplot as plt

# Parametri del sistema
tau = 1  # Costante di tempo
t_final = 5 * tau  # Tempo finale per il grafico
t = np.linspace(0, t_final, 500)  # Tempo discreto

# Risposta al gradino del sistema del primo ordine
response = 1 - np.exp(-t / tau)

# Calcolo della retta tangente
tangent_line = t / tau

# Calcolo dei punti caratteristici
t_tau = tau
t_2tau = 2 * tau
t_3tau = 3 * tau
response_tau = 1 - np.exp(-1)
response_2tau = 1 - np.exp(-2)
response_3tau = 1 - np.exp(-3)

# Creazione del grafico
plt.figure(figsize=(10, 6))

# Risposta al gradino
plt.plot(t, response, label="Risposta al gradino", color="black")

# Retta tangente
plt.plot(t, tangent_line, linestyle="--", color="gray", label="Retta tangente in t=0")

# Linea orizzontale al valore finale
plt.axhline(y=1, color="gray", linestyle="--", label="Valore finale")

# Evidenziazione di t=tau, 2tau, 3tau
plt.scatter([t_tau, t_2tau, t_3tau], [response_tau, response_2tau, response_3tau], color="black", label="Punti caratteristici", zorder=5)
plt.axvline(x=t_tau, color="gray", linestyle="--", label="t=τ")
plt.axvline(x=t_2tau, color="gray", linestyle="--", label="t=2τ")
plt.axvline(x=t_3tau, color="gray", linestyle="--", label="t=3τ")

# Annotazioni per i punti caratteristici
plt.text(t_tau + 0.25, response_tau, f"τ ({response_tau:.2f})", color="black", fontsize=10, ha='center')
plt.text(t_2tau + 0.25, response_2tau + 0.05, f"2τ ({response_2tau:.2f})", color="black", fontsize=10, ha='center')
plt.text(t_3tau + 0.25, response_3tau - 0.05, f"3τ ({response_3tau:.2f})", color="black", fontsize=10, ha='center')

# Etichette e titolo
#plt.title("Risposta al gradino di un sistema del primo ordine", fontsize=14)
#plt.xlabel("Tempo t", fontsize=12)
#plt.ylabel("Ampiezza", fontsize=12)
#plt.legend()
#plt.grid()

# Limiti dell'asse verticale
plt.ylim(0, 1.02)

plt.savefig("risposta_gradino_ord1_tempo.png", dpi=300)

# Mostra il grafico
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Imposta il tema in scala di grigi
plt.style.use('grayscale')

# Intervallo di x
x = np.linspace(0, 0.5, 100)

# Definizione delle funzioni
C_v = 1 / (1 - x)
C_a = 1 / (x * (1 - x))
C_aRMS = np.sqrt(x) / (x * (1 - x))

# Punto specifico x = 1/3
x_point = 1 / 3
C_v_point = 1 / (1 - x_point)
C_a_point = 1 / (x_point * (1 - x_point))
C_aRMS_point = np.sqrt(x_point) / (x_point * (1 - x_point))

# Creazione del grafico
plt.figure(figsize=(10, 6))
plt.plot(x, C_v, color='black', linestyle='-', label='C v')
plt.plot(x, C_a, color='dimgray', linestyle='-', label='C a')
plt.plot(x, C_aRMS, color='darkgray', linestyle='-', label='C a RMS')

# Aggiungi una linea verticale in x = 1/3
plt.axvline(x=x_point, color='lightgray', linestyle='--', label='x = 1/3')

# Aggiungi marcatori per i valori delle funzioni in x = 1/3
plt.scatter([x_point], [C_v_point], color='black', edgecolor='gray', zorder=5)
plt.scatter([x_point], [C_a_point], color='dimgray', edgecolor='gray', zorder=5)
plt.scatter([x_point], [C_aRMS_point], color='darkgray', edgecolor='gray', zorder=5)

# Annotazioni per i valori delle funzioni in x = 1/3
plt.text(x_point, C_v_point, f'{C_v_point:.2f}', color='black', ha='left', va='bottom')
plt.text(x_point, C_a_point, f'{C_a_point:.2f}', color='dimgray', ha='left', va='bottom')
plt.text(x_point, C_aRMS_point, f'{C_aRMS_point:.2f}', color='darkgray', ha='left', va='bottom')

# Personalizzazione del grafico
#plt.title("C v, C a, e C a RMS per moto simmetrico con evidenza di x = 1/3")
plt.xlabel("λ")
plt.ylabel("C")
plt.ylim(0, 10)  # Imposta il limite dell'asse y tra 0 e 10
plt.legend()
plt.grid(True)

# Salva il grafico come immagine
plt.savefig("CvCaCaRMS.png", dpi=300)
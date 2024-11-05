import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definizione della funzione con limite massimo
def f(lambda_A, lambda_D):
    with np.errstate(divide='ignore', invalid='ignore'):
        result = (1 / lambda_A) * (1 / (1 - (lambda_A + lambda_D) / 2)) * np.sqrt(lambda_A + (lambda_A ** 2) / lambda_D)
    result = np.nan_to_num(result, nan=np.inf, posinf=np.inf, neginf=-np.inf)
    # Limitiamo i valori della funzione al massimo di 10
    result = np.clip(result, None, 10)
    return result

# Creazione di una griglia di valori per lambda_A e lambda_D tra 0 e 1
lambda_A = np.linspace(0.1, 1, 100)
lambda_D = np.linspace(0.1, 1, 100)
lambda_A, lambda_D = np.meshgrid(lambda_A, lambda_D)

# Calcolo della funzione sulla griglia con limite applicato
Z = f(lambda_A, lambda_D)

# Coordinate del minimo previsto (λ_A, λ_D) = (1/3, 1/3)
min_lambda_A = 1/3
min_lambda_D = 1/3
min_value = f(min_lambda_A, min_lambda_D)

# Creazione del grafico 3D in scala di grigi
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plotting della superficie con scala di grigi
ax.plot_surface(lambda_A, lambda_D, Z, cmap='gray', edgecolor='none', alpha=0.8)

# Evidenziazione del minimo
ax.scatter(min_lambda_A, min_lambda_D, min_value, color='red', s=50, label='Minimo')
ax.set_xlabel('λ_A')
ax.set_ylabel('λ_D')
ax.set_zlabel('C a RMS(λ_A, λ_D)')
#ax.set_title('C a RMS')

# Aggiunta della legenda
ax.legend()

# Salva il grafico come immagine
plt.savefig("CaRMS.png", dpi=300)
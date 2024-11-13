import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def spline_434(times, positions):
    """
    Calcola una SPLine 434: combinazione di polinomi di grado 3 e 4.

    Parameters:
    - times: array-like, istanti di tempo corrispondenti ai punti noti
    - positions: array-like, posizioni verticali corrispondenti ai punti noti

    Returns:
    - splines: lista di funzioni polinomiali (una per ogni intervallo)
    """
    n = len(times) - 1
    splines = []

    for i in range(n):
        # Intervallo corrente
        t0, t1 = times[i], times[i+1]
        p0, p1 = positions[i], positions[i+1]

        # Calcolo velocità iniziale e finale
        v0 = 0 if i == 0 else (positions[i] - positions[i-1]) / (times[i] - times[i-1])
        v1 = 0 if i == n - 1 else (positions[i+1] - positions[i]) / (times[i+1] - times[i])

        # Durata dell'intervallo
        dt = t1 - t0

        # Condizioni iniziali e finali
        # p(t0) = p0, p(t1) = p1, v(t0) = v0, v(t1) = v1
        # Usa polinomi di grado 4 per garantire continuità di posizione e velocità
        A = np.array([
            [1, t0, t0**2, t0**3, t0**4],  # p(t0) = p0
            [0, 1,  2*t0, 3*t0**2, 4*t0**3],  # v(t0) = v0
            [1, t1, t1**2, t1**3, t1**4],  # p(t1) = p1
            [0, 1,  2*t1, 3*t1**2, 4*t1**3],  # v(t1) = v1
            [0, 0,    2,    6*t0, 12*t0**2]  # a(t0) continuo
        ])
        b = np.array([p0, v0, p1, v1, 0])  # Condizioni

        coeffs = np.linalg.solve(A, b)
        splines.append(coeffs)

    return splines

def eval_spline(coeffs, t):
    """Valuta una spline (polinomio di grado 4) dato un tempo t."""
    return coeffs[0] + coeffs[1]*t + coeffs[2]*t**2 + coeffs[3]*t**3 + coeffs[4]*t**4

def plot_spline_434(times, positions, splines, resolution=1000):
    """
    Traccia la SPLine 434 e i punti noti.

    Parameters:
    - times: array-like, istanti di tempo corrispondenti ai punti noti
    - positions: array-like, posizioni verticali corrispondenti ai punti noti
    - splines: lista di coefficienti dei polinomi spline 434
    - resolution: int, numero di punti per la grafica della spline
    """
    t_dense = np.linspace(min(times), max(times), resolution)
    p_dense = np.zeros_like(t_dense)

    for i, t in enumerate(t_dense):
        # Determina l'intervallo corrente
        for j in range(len(times) - 1):
            if times[j] <= t <= times[j+1]:
                coeffs = splines[j]
                p_dense[i] = eval_spline(coeffs, t)
                break

    # Grafico
    plt.figure(figsize=(10, 6))
    plt.plot(t_dense, p_dense, label='SPLine 434', color='black')
    plt.scatter(times, positions, color='grey', label='Punti Noti')
    plt.ylabel('q')
    plt.savefig("SPLine_v2.png", dpi=300)
    plt.show()

# Esempio di utilizzo
if __name__ == "__main__":
    # Punti noti: istanti di tempo e posizioni verticali
    times = [0, 1, 2, 3, 4]  # Istanti di tempo
    positions = [0, 2, -1, 3, 0]  # Posizioni verticali

    # Calcolo della SPLine 434
    splines = spline_434(times, positions)

    # Traccia la SPLine 434
    plot_spline_434(times, positions, splines)

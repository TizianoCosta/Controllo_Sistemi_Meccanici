import numpy as np
import matplotlib.pyplot as plt

# Parametri noti
P1 = 10  # Altezza finale del primo tratto
v = 2    # Velocità costante nel secondo tratto
T1 = 2   # Durata del primo tratto
T2 = 5   # Durata del secondo tratto
T3 = 3   # Durata del terzo tratto

# Primo tratto: Polinomio di terzo grado
def poly3_first(t):
    a3 = - 2 * P1 / T1**3 + v / T1**2
    a2 = 3 * P1 / T1**2 - v / T1
    return a3 * t**3 + a2 * t**2

def poly3_first_vel(t):
    a3 = - 2 * P1 / T1**3 + v / T1**2
    a2 = 3 * P1 / T1**2 - v / T1
    return 3 * a3 * t**2 + 2 * a2 * t

def poly3_first_acc(t):
    a3 = - 2 * P1 / T1**3 + v / T1**2
    a2 = 3 * P1 / T1**2 - v / T1
    return 6 * a3 * t + 2 * a2

# Secondo tratto: Velocità costante
def constant(t):
    return P1 + v * (t - T1)

def constant_vel(t):
    return np.full_like(t, v)

def constant_acc(t):
    return np.zeros_like(t)

# Terzo tratto: Polinomio di terzo grado
def poly3_last(t):
    t_rel = t - (T1 + T2)
    P2 = P1 + v * T2  # Posizione iniziale del terzo tratto
    b3 = 2 * (P2 + v * T3) / T3**3 - v / T3**2
    b2 = - 3 * (P2 + v * T3) / T3**2 + v / T3
    b1 = v
    b0 = P2
    return b3 * t_rel**3 + b2 * t_rel**2 + b1 * t_rel + b0

def poly3_last_vel(t):
    t_rel = t - (T1 + T2)
    P2 = P1 + v * T2
    b3 = 2 * (P2 + v * T3) / T3**3 - v / T3**2
    b2 = - 3 * (P2 + v * T3) / T3**2 + v / T3
    b1 = v
    return 3 * b3 * t_rel**2 + 2 * b2 * t_rel + b1

def poly3_last_acc(t):
    t_rel = t - (T1 + T2)
    P2 = P1 + v * T2
    b3 = 2 * (P2 + v * T3) / T3**3 - v / T3**2
    b2 = - 3 * (P2 + v * T3) / T3**2 + v / T3
    return 6 * b3 * t_rel + 2 * b2

# Time vectors for each segment
t1 = np.linspace(0, T1, 100)
t2 = np.linspace(T1, T1 + T2, 100)
t3 = np.linspace(T1 + T2, T1 + T2 + T3, 100)

# Compute position, velocity, and acceleration
s1 = poly3_first(t1)
v1 = poly3_first_vel(t1)
a1 = poly3_first_acc(t1)

s2 = constant(t2)
v2 = constant_vel(t2)
a2 = constant_acc(t2)

s3 = poly3_last(t3)
v3 = poly3_last_vel(t3)
a3 = poly3_last_acc(t3)

# Combine results
t = np.concatenate([t1, t2, t3])
s = np.concatenate([s1, s2, s3])
v = np.concatenate([v1, v2, v3])
a = np.concatenate([a1, a2, a3])

# Plot the results
plt.figure(figsize=(12, 8))

# Posizione
plt.subplot(3, 1, 1)
plt.plot(t, s, label="Posizione", color="black")
plt.ylabel("q")

# Velocità
plt.subplot(3, 1, 2)
plt.plot(t, v, label="Velocità", color="black")
plt.ylabel("V")

# Accelerazione
plt.subplot(3, 1, 3)
plt.plot(t, a, label="Accelerazione", color="black")
plt.ylabel("A")


plt.subplots_adjust(hspace=0.2)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("tratti_vel_cost.png", dpi=300)
plt.show()
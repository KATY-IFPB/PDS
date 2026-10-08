import numpy as np
import matplotlib.pyplot as plt

# --- Exemplo 1: Sinal de Energia x1[n] = (0.8)^n * u[n] ---
n1 = np.arange(0, 100)  # Aproximação de n=0 a infinito
x1 = (0.8)**n1

# Cálculo numérico da energia
E1_num = np.sum(np.abs(x1)**2)
print(f"Exemplo 1 - Energia Numérica: {E1_num:.4f} (Teórico: {25/9:.4f})")

# --- Exemplo 2: Sinal de Potência x2[n] = cos(pi/2 * n) ---
n2 = np.arange(-100, 101)  # Intervalo de -N a N com N=100
x2 = np.cos(np.pi / 2 * n2)

# Cálculo numérico da potência média P = lim (1 / (2N + 1)) * sum(|x[n]|^2)
N = 100
P2_num = (1 / (2 * N + 1)) * np.sum(np.abs(x2)**2)
print(f"Exemplo 2 - Potência Numérica: {P2_num:.4f} (Teórico: 0.5000)")

# --- Plotagem dos Gráficos ---
plt.figure(figsize=(12, 5))

# Gráfico 1: Sinal de Energia
plt.subplot(1, 2, 1)
markerline, stemlines, baseline = plt.stem(n1[:20], x1[:20])
plt.title(r'Sinal de Energia: x1[n]=0.8nu[n]')
plt.xlabel('n')
plt.ylabel('x1[n]')
plt.grid(True)

# Gráfico 2: Sinal de Potência
plt.subplot(1, 2, 2)
markerline, stemlines, baseline = plt.stem(n2[90:111], x2[90:111])
plt.title(r'Sinal de Potência: x2[n]=(n/2)')
plt.xlabel('n')
plt.ylabel('x2[n]')
plt.grid(True)

plt.tight_layout()
plt.show()



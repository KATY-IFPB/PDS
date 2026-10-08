import numpy as np
import matplotlib.pyplot as plt

# --- Definição dos Sinais de Entrada e Respostas ao Impulso ---
x = np.array([1, 2, 1])
h1 = np.array([1, 1])    	# Experimento 1 (Orientador)
h2 = np.array([1, -1])   	# Experimento 2 (Modificado)

# --- Cálculo Computacional da Convolução ---
y1 = np.convolve(x, h1)
y2 = np.convolve(x, h2)

print("Resultado do Experimento 1 (Python):", y1)
print("Resultado do Experimento 2 (Python):", y2)

# --- Eixos Temporais ---
n_x = np.arange(len(x))
n_h1 = np.arange(len(h1))
n_h2 = np.arange(len(h2))
n_y1 = np.arange(len(y1))
n_y2 = np.arange(len(y2))

# --- Plotagem dos Sinais ---
fig, axes = plt.subplots(3, 2, figsize=(10, 7.5))

# Coluna 1: Experimento 1 (h1[n] = {1, 1})
axes[0, 0].stem(n_x, x)
axes[0, 0].set_title("Entrada x[n] = {1, 2, 1}")
axes[0, 0].set_ylabel("Amplitude")

axes[1, 0].stem(n_h1, h1, linefmt='r-', markerfmt='ro')
axes[1, 0].set_title("Resposta ao Impulso h1[n] = {1, 1}")
axes[1, 0].set_ylabel("Amplitude")

axes[2, 0].stem(n_y1, y1, linefmt='g-', markerfmt='go')
axes[2, 0].set_title("Saída y1[n] = x[n] * h1[n]")
axes[2, 0].set_xlabel("n")
axes[2, 0].set_ylabel("Amplitude")

# Coluna 2: Experimento 2 (h2[n] = {1, -1})
axes[0, 1].stem(n_x, x)
axes[0, 1].set_title("Entrada x[n] = {1, 2, 1}")

axes[1, 1].stem(n_h2, h2, linefmt='r-', markerfmt='ro')
axes[1, 1].set_title("Resposta ao Impulso h2[n] = {1, -1}")

axes[2, 1].stem(n_y2, y2, linefmt='g-', markerfmt='go')
axes[2, 1].set_title("Saída y2[n] = x[n] * h2[n]")
axes[2, 1].set_xlabel("n")

for ax in axes.flat:
	ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()



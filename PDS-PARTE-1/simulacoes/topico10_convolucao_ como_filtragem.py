import numpy as np
import matplotlib.pyplot as plt

# Semear gerador para reprodutibilidade
np.random.seed(42)

# 1. Vetor de tempo discreto
n = np.arange(0, 80)

# 2. Sinal Original Limpo (Pulso e Degrau)
x_limpo = np.zeros_like(n, dtype=float)
x_limpo[15:35] = 1.0  # Pulso
x_limpo[50:70] = 0.6  # Degrau

# 3. Sinal Contaminado (Ruído Aditivo Gaussiano, sigma = 0.15)
ruido = np.random.normal(loc=0.0, scale=0.15, size=len(n))
x_ruidoso = x_limpo + ruido

# 4. Filtros de Média Móvel (M = 3, M = 5, M = 10)
valores_M = [3, 5, 10]
sinais_filtrados = {}
h_filtros = {}

for M in valores_M:
	h = np.ones(M) / M
	h_filtros[M] = h
	# Convolução causal truncada no comprimento de n
	sinais_filtrados[M] = np.convolve(x_ruidoso, h, mode='full')[:len(n)]

# --- Visualização 1: Filtragem do Sinal ---
plt.figure(figsize=(14, 9))

# Subplot 1: Sinais de Entrada
plt.subplot(4, 1, 1)
plt.plot(n, x_limpo, 'k--', linewidth=2, label='Sinal Original x[n]')
plt.plot(n, x_ruidoso, color='gray', alpha=0.7, label='Sinal Contaminado $x_{\\text{ruidoso}}[n]$')
plt.title('Sinais de Entrada: Original (Ideal) vs. Contaminado com Ruído Gaussiano')
plt.ylabel('Amplitude')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper right')

# Subplots 2, 3 e 4: Resultados para M = 3, 5, 10
cores = ['blue', 'green', 'red']
for idx, M in enumerate(valores_M):
	plt.subplot(4, 1, idx + 2)
	plt.plot(n, x_limpo, 'k--', alpha=0.5, label='Original Limpo')
	plt.plot(n, sinais_filtrados[M], color=cores[idx], linewidth=2, label=f'Filtrado (M=M)')
	plt.title(f'Sinal Filtrado com Média Móvel M=M')
	plt.ylabel('Amplitude')
	plt.grid(True, linestyle='--', alpha=0.5)
	plt.legend(loc='upper right')

plt.xlabel('Amostras (n)')
plt.tight_layout()
plt.show()

# --- Visualização 2: Respostas ao Impulso h[n] ---
plt.figure(figsize=(12, 3))
for idx, M in enumerate(valores_M):
	plt.subplot(1, 3, idx + 1)
	n_h = np.arange(M)
	plt.stem(n_h, h_filtros[M])
	plt.title(f'Resposta ao Impulso h[n] (M=M)')
	plt.xlabel('n')
	plt.ylabel('h[n]')
	plt.ylim(0, 0.4)
	plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()



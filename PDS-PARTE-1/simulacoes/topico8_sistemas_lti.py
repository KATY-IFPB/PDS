import numpy as np
import matplotlib.pyplot as plt

# Definição dos sinais finitos do exemplo
x = np.array([2, 3])   	# Entrada x[n] para n = 0, 1
h = np.array([1, 1, 1])	# Resposta ao impulso h[n] para n = 0, 1, 2

# Convolução discreta y[n] = x[n] * h[n]
y = np.convolve(x, h)

# Eixos temporais
n_x = np.arange(0, len(x))
n_h = np.arange(0, len(h))
n_y = np.arange(0, len(y))

# Plotagem dos gráficos
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.stem(n_x, x)
plt.title(r'Entrada x[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(1, 3, 2)
plt.stem(n_h, h)
plt.title(r'Resposta ao Impulso h[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.stem(n_y, y)
plt.title(r'Saída Convoluída y[n]=x[n]*h[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()



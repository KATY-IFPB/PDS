import numpy as np

# Definição dos 5 sistemas
systems = {
	"1. y[n] = 2x[n]": lambda x, n: 2 * x,
	"2. y[n] = x[n] + x[n-1]": lambda x, n: x + np.roll(x, 1),
	"3. y[n] = x[n]^2": lambda x, n: x**2,
	"4. y[n] = x[n+1]": lambda x, n: np.roll(x, -1),
	"5. y[n] = n*x[n]": lambda x, n: n * x
}

# Parâmetros de teste
n = np.arange(-10, 11)
x1 = np.sin(np.pi / 4 * n)
x2 = np.cos(np.pi / 3 * n)
a, b = 2.0, 3.0
n0 = 2

print(f"{'Sistema':<25} | {'Linear?':<10} | {'Invariante no Tempo?':<20}")
print("-" * 60)

for name, sys in systems.items():
	# Teste de Linearidade: T{a*x1 + b*x2} vs a*T{x1} + b*T{x2}
	y_comb = sys(a * x1 + b * x2, n)
	y_lin = a * sys(x1, n) + b * sys(x2, n)
	is_linear = np.allclose(y_comb[2:-2], y_lin[2:-2])
    
	# Teste de Invariância no Tempo: T{x[n-n0]} vs y[n-n0]
	x1_shift = np.roll(x1, n0)
	y1_shift = sys(x1_shift, n)
	y_orig_shift = np.roll(sys(x1, n), n0)
	is_time_invariant = np.allclose(y1_shift[4:-4], y_orig_shift[4:-4])
    
	lin_str = "Sim" if is_linear else "Não"
	ti_str = "Sim" if is_time_invariant else "Não"
	print(f"{name:<25} | {lin_str:<10} | {ti_str:<20}")



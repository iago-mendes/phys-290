# Iago Braz Mendes (T01362926)
# Physics 290 (Computational Modeling)
# Oberlin College
# Spring 2023

import numpy as np
import matplotlib.pyplot as plt

def Pi(N):
	x = np.random.uniform(0, 1, N)
	return np.mean(4 * np.sqrt(1 - x**2))

N = [int(1e1), int(1e2), int(1e3), int(1e4), int(1e5), int(1e6)] # Number of samples
S = [] # Standard deviation

for n in N:
	results = []
	for i in range(100):
		results.append(Pi(n))
	S.append(np.std(results))

x = np.log(N)
y = np.log(S)

m = (np.mean(x*y) - np.mean(x)*np.mean(y)) / (np.mean(x**2) - np.mean(x)**2)
print('m = p =', m)

b = np.mean(y) - np.mean(x) * (np.mean(y*x) - np.mean(y)*np.mean(x)) / (np.mean(x**2) - np.mean(x)**2)
print('b = log(k) =', b)

plt.scatter(x, y, label='Data points')
plt.plot(x, m*x + b, label=r'Linear fit: $\log (\sigma) = $' + str(round(m, 2)) + r' $\log (N) + $' + str(round(b, 2)))
plt.plot(x, -.5*x, label=r'Expected fit: $\log (\sigma) = $' + str(-.5) + r' $\log (N) + $' + str(0))

plt.xlabel(r'$\log (N)$')
plt.ylabel(r'$\log (\sigma)$')
plt.legend()
plt.title('Error convergence in Monte Carlo integration')

plt.show()

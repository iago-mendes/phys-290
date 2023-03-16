# Iago Braz Mendes (T01362926)
# Physics 290 (Computational Modeling)
# Oberlin College
# Spring 2023

import numpy as np
from scipy.special import j0

def rho(x, y, z):
	return 4 + x**3 + 3 * y * j0(z)

Nsamples = int(1e6)

x = np.random.uniform(-1, 1, Nsamples)
y = np.random.uniform(-1, 1, Nsamples)
z = np.random.uniform(-1, 1, Nsamples)
DomainSize = 2.

M = DomainSize**3 * np.mean(rho(x, y, z))
print('M =', M)

Ix = DomainSize**3 * np.mean(x * rho(x, y, z))
print('Xcom =', Ix / M)

Iy = DomainSize**3 * np.mean(y * rho(x, y, z))
print('Ycom =', Iy / M)

Iz = DomainSize**3 * np.mean(z * rho(x, y, z))
print('Zcom =', Iz / M)

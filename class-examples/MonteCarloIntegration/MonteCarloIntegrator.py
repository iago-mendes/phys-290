import numpy as np

N = int(1e6)

x = np.random.uniform(-1, 1, N)
DomainSize = 2.

fmean = np.mean(np.sqrt(1. - x**2))

Integral = 2. * DomainSize * fmean
print("Pi integral: ", Integral)

fsquaredmean = np.mean(1 - x**2)
uncertainty = 2. * DomainSize * np.sqrt((fsquaredmean - fmean)**2 / N)
print("Uncertainty: ", uncertainty)

print("Actual error: ", Integral - np.pi)
print("Error / Uncertainty: ", (Integral - np.pi) / uncertainty)

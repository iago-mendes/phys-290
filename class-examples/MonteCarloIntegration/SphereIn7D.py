import numpy as np

N = int(1e8)

x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)
z = np.random.uniform(-1, 1, N)
w = np.random.uniform(-1, 1, N)
v = np.random.uniform(-1, 1, N)
u = np.random.uniform(-1, 1, N)
t = np.random.uniform(-1, 1, N)

N_in = len(x[x**2 + y**2 + z**2 + w**2 + v**2 + u**2 + t**2 < 1])

print((N_in / N) * 2**7)

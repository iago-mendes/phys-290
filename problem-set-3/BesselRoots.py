import numpy as np
from scipy.special import *
import matplotlib.pyplot as plt

roughroots = []

x = 0.

while (len(roughroots) < 20):
	if (j0(x) * j0(x - .1) < 0):
		roughroots.append(x)
	x += .1

polishedroots = np.array(roughroots)

for i in range(10):
	polishedroots += j0(polishedroots) / j1(polishedroots)

print(polishedroots)

xs = []
x = 0.
while (x <= 70):
	xs.append(x)
	x += .01

plt.plot(xs, j0(xs), label="J_0(x)", color="blue")
plt.scatter(roughroots, j0(roughroots), label="Rough Roots", marker="x", color="red")
plt.scatter(polishedroots, j0(polishedroots), label="Polished Roots", color="green")
plt.legend()
plt.show()

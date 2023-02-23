import numpy as np
import matplotlib.pyplot as plt

def F(a, x):
	return a*x*(1-x)

def IterateF(initialval, n_its, a):
	x0 = initialval
	for i in range(n_its):
		x0 = F(a, x0)
		print(x0)

IterateF(.4, 100000, 3.84)

x = np.linspace(0, 1, 500)

# for a in np.linspace(0, 3, 10):
# 	plt.plot(x, F(a, x))

a = 3.84
plt.plot(x, F(a, x))
plt.plot(x, F(a, F(a, x)))
plt.plot(x, F(a, F(a, F(a, F(a, x)))))

plt.plot(x, x)
plt.show()

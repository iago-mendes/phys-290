import numpy as np

a = 10

def f(x):
	return a * np.cos(x)

x = .1
for i in range(100):
	x = f(x)
	print(x)

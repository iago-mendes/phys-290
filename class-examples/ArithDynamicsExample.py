import numpy as np

Q = 4

x = 2.01

def F(x):
	return Q/x

for i in range(50):
	x = F(x)
	print(x)

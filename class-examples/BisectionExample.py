xL = 0
xR = 2

def f(x):
	return x**2 - 2

def Bisection(F, xL, xR, accuracy_target):
	if (xR < xL):
		print("Error, xR must be greater than xL!")
		return
	
	for i in range(100):
		xC = .5 * (xL + xR)
		if (F(xL) * F(xC) < 0):
			xR = xC
		elif (F(xC) * F(xR) < 0):
			xL = xC
		
		error = .5*(xR - xL)

		print(f'{i}: {.5*(xL + xR)} +/- {error}')

		if (error < accuracy_target):
			break

Bisection(f, 0, 2, 1e-15)

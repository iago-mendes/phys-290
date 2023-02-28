import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.animation import FuncAnimation 

def LogMap(x, a):
	return a * x * (1 - x)

Na = 5000
Nx = 1000

def CreateLogMapBifurcation(Niterations):
	a_list = []
	x_list = []

	# compute fixed points
	counter = 0
	for a in np.linspace(0., 4., Na):
		x = np.linspace(0, 1, Nx)

		counter += 1
		if (counter % 100 == 0):
			print("a =", a)

		for i in range(Niterations):
			x = LogMap(x, a)
		
		a_list = np.append(a_list, a * np.ones_like(x))
		x_list = np.append(x_list, x)

	# constuct image from data
	imagematrix = np.zeros((Nx, Na))
	for i in range(np.size(x_list)):
		xind = int(x_list[i] * Nx / 1.)
		aind = int(a_list[i] * Na / 4.)
		if(xind < Nx and aind < Na):
			imagematrix[xind, aind] += 1

	# fix saturation
	saturation = 1
	imagematrix = np.arcsinh(imagematrix/saturation)

	# normalize
	imagematrix /= np.max(imagematrix)

	# output result
	plt.imshow(imagematrix, cmap='coolwarm', extent=(0,4,0,1), origin='lower')
	plt.title('Logistic Map Bifurcation')
	plt.xlabel('a value')
	plt.ylabel(f'x after {Niterations} iterations')
	plt.show()

CreateLogMapBifurcation(5)
CreateLogMapBifurcation(10)
CreateLogMapBifurcation(100)
CreateLogMapBifurcation(1000)

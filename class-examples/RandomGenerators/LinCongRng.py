
# This code defines a "Linear Congruential" pseudorandom number generator, 
# both with integer output and floating-point output. It checks the quality 
# of the numbers using a histogram, autocorrelation, and an image of 
# sequential pairs. And it looks good at least on these counts.
#
# Rob Owen, ph290, Oberlin College, Spring 2023

seed = 2514736251

def LCG(): #Linear congruential generator.
	global seed
	x = seed
	x = x*837462 + 9387456 # Arbitrary numbers.
	x = x%int(1.e10)
	seed = x
	return x

def LCGF(): #Linear congruential generator -- float.
	return float(LCG())/1.e10


# Produce a long list of numbers from this generator:
rlist = []
for i in range(10000):
	rlist.append(LCGF())

# Plot a histogram of those numbers:
import matplotlib.pyplot as plt
plt.hist(rlist, 20)
plt.show()

# Plot the autocorrelation of the numbers:
import numpy as np
a = np.array(rlist)-.5 #set the mean to zero
plt.acorr(a, maxlags=100)
plt.show()

# Produce a 2-d scatter of sample points:
xlist = []
ylist = []

for i in range(5000):
	xlist.append(LCGF())
	ylist.append(LCGF())

plt.scatter(xlist, ylist, s=.05)
plt.show()

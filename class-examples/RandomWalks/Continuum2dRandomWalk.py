
# Code to carry out a single random walk in two dimensions, and plot the path.
#
# Rob Owen, ph290, Oberlin College, Spring 2023

import numpy as np 
import matplotlib.pyplot as plt

Nsteps = int(input('How many steps? '))
x = 0. # This time we treat the x and y coordinates as floats.
y = 0.

xlist = [x]
ylist = [y]
#for i in range(Nsteps):
#    r1 = np.random.normal(0.,1.) # Gives a nonuniform (Gaussian) random 
#                                 # number, with mean 0 and variance 1.
#    r2 = np.random.normal(0.,1.)
#    x += r1 
#    y += r2 
#    xlist.append(x) # For plotting.
#    ylist.append(y)

# Vectorized version:
xlist = np.cumsum(np.random.normal(0.,1.,Nsteps))
ylist = np.cumsum(np.random.normal(0.,1.,Nsteps))
xlist = np.append([0], xlist)
ylist = np.append([0], ylist)

print('Final location =', xlist[-1], ylist[-1])
print('Final distance =', (xlist[-1]**2+ylist[-1]**2)**.5)

xmax = np.max(np.abs(xlist))
ymax = np.max(np.abs(ylist))
range = 1.05*np.max([xmax,ymax]) #Make plot a little wider than needed.
plt.axis([-range,range,-range,range])
plt.title("Two Dimensional continuum Random Walk")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xlist, ylist, linewidth = 1)
plt.show()

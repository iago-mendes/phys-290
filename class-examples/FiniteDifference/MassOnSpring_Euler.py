
# This code integrates Newton's second law, for a mass on a spring, using 
# Euler's method, and shows the oscillatory behavior.
#
# Rob Owen, ph290, Oberlin College, Fall 2023

import numpy as np
import matplotlib.pyplot as plt

# Define parameters:
k = 1.
m = 1.
b = 0.

# The right-hand-sides of the coupled ODEs:
def fx(x, v, t):
    return v

def fv(x, v, t):
    return -k*x/m - b*v/m  #The b term would represent frictional damping.

# Note that the 't' argument is unnecessary in the above, since the ODEs 
# don't have explicit time dependence. However, if they did (as, from a 
# driving force), then this framework would allow it.


dt = .001
t = np.arange(0.,100., dt)

x0 = 1.
v0 = 0.
x = np.array([x0]) # Start with just the initial data.
v = np.array([v0])

while len(x)<len(t): # Run until you have an x for every t.
    xnew = x[-1] + dt*fx(x[-1],v[-1],t[len(x)])
    vnew = v[-1] + dt*fv(x[-1],v[-1],t[len(x)])
    x = np.append(x, xnew)
    v = np.append(v, vnew)
    # Note x[-1] means the last element in the current x array, and 
    # similarly for v[-1]. 
    # It's important that we computed xnew and vnew 
    # before appending anything to the x and v arrays. 
    # If we had simply done:
    # x = np.append(x, x[-1]+dt*fx(x[-1],v[-1])
    # v = np.append(v, v[-1]+dt*fv(x[-1],v[-1])
    # then the x that goes into fv will be the one from the *current* timestep,
    # not the previous one. Errors like this could affect accuracy, or 
    # even stability. 


plt.plot(t, x)
plt.title("mass on spring system, Euler's method")
plt.xlabel("time")
plt.ylabel("displacement")
plt.show()
# When running, note that the amplitude grows in time. This nonconservation 
# of energy is due to the discretization error. Reducing the timestep (or using 
# a more accurate method) improves this error.


plt.plot(t, x - x[0]*np.cos(t*np.sqrt(k/m)))
plt.title("error in computed solution, assuming no damping")
plt.xlabel("time")
plt.ylabel("x_computed - x_exact")
plt.show()

plt.plot(t, .5*m*v**2 + .5*k*x**2)
plt.title("Total system energy.")
plt.xlabel("time")
plt.ylabel("K + U")
plt.show()

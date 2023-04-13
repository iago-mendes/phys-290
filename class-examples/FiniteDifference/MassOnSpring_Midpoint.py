
# This code evolves the mass-on-spring problem using the second-order accurate
# "midpoint method" (also known as Runge-Kutta 2). 
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
    return -k*x/m - b*v/m #The b term would represent frictional damping.

dt = .001 
t = np.arange(0.,20., dt)

x0 = 1.
v0 = 0.
x = np.array([x0]) # Start with just the initial data.
v = np.array([v0])

while len(x)<len(t): # Run until you have an x for every t.
    xnew = x[-1] + dt*fx(x[-1]+.5*dt*fx(x[-1],v[-1],t[len(x)]),
                         v[-1]+.5*dt*fv(x[-1],v[-1],t[len(x)]),
                         t[len(x)]+.5*dt)

    vnew = v[-1] + dt*fv(x[-1]+.5*dt*fx(x[-1],v[-1],t[len(x)]),
                         v[-1]+.5*dt*fv(x[-1],v[-1],t[len(x)]),
                         t[len(x)]+.5*dt)
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
    # not the previous one. Errors like this could affect accuracy. 


plt.plot(t, x)
plt.ylim(-1.5,1.5)
plt.title("mass on spring system, Midpoint method")
plt.xlabel("time")
plt.ylabel("displacement")
plt.show()


plt.plot(t, x-x[0]*np.cos(k*t/m))
plt.title("error in computed solution")
plt.xlabel("time")
plt.ylabel("x_computed - x_exact")
plt.show()


plt.plot(t, .5*m*v**2 + .5*k*x**2)
plt.title("Total system energy")
plt.xlabel("time")
plt.ylabel("K + U")
plt.show()

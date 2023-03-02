
# Code to carry out a large number of simple random walks and print out 
# basic statistics of the final location.
#
# Rob Owen, ph290, Oberlin College, Sprint 2023

import numpy as np 

def RandomWalk(Nsteps): # Function that carries out a random walk.
#    x = 0
#    for i in range(Nsteps):
#        r = np.random.randint(0,2) # Gives a random integer, zero or one.
#        x += (-1)**r # If r==0 go right, if r==1 go left.
### The above 4 lines are the non-vectorized way of doing this. The vectorized
### approach below is much more efficient.

    r = np.random.randint(0,2,Nsteps) # Generate Nsteps randum numbers simultaneously.
    x = np.sum((-1.)**r) # Turn them into -1 or 1, and take the sum
    return x # Return the final position.

Nsteps = int(input('How many steps per trial? '))
Ntrials = int(input('How many trials? '))

xarray = np.array([])

for i in range(Ntrials):
    xarray = np.append(xarray, RandomWalk(Nsteps)) 
        #(Appending works a little differently for numpy arrays than for lists.)

print("Average final x is:", xarray.mean())
print("Root-mean-square final x is:", np.sqrt((xarray**2).mean()))

import matplotlib.pyplot as plt
plt.hist(xarray, 20)
plt.show()

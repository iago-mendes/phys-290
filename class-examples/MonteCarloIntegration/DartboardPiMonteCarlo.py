
# A simple code to compute pi by "dartboard Monte Carlo" integration.
# Below I've implemented the algorithm in a simple non-vectorized loop
# approach (which is quite slow and complicated to read), and in a
# vectorized approach (approximately 100x faster and simpler to read
# and code apart from one slightly obscure step).
#
# Rob Owen, physics 290, Spring 2023

import numpy as np



# First, a non-vectorized approach:
def PiMC_nv(N):
    N = int(N) #Turn it into an integer so that other functions don't get confused
    print(N)
    N_in = 0 # Initialize a counter.

    for i in range(N):
        if(i%10000==0):
            print(100.*i/N, "percent complete.")
        x = np.random.uniform(-1,1)
        y = np.random.uniform(-1,1)
        if(x**2+y**2<1):
            N_in += 1
    return 4.*N_in/N


# print("Volume =", PiMC_nv(1e6))


## And a vectorized approach:
def PiMC_v(N):
    N = int(N)
    x = np.random.uniform(-1,1,N)
    y = np.random.uniform(-1,1,N)
    N_in = len(x[x**2+y**2<1])
    # The above line is the key to the calculation, and it employs a really
    # useful bit of python structure: conditional slicing.
    # A 'slice' is a subset of a list or an array.
    # A 'conditional slice' is a slice determined by a condition on the elements.
    # The length of a conditionally sliced array is the number of elements
    # that satisfy that condition.
    return 4.*N_in/N

# print("Volume =", PiMC_v(1e8))


## To get better statistics, let's repeat the vectorized function 100 times:
piarray = []
for i in range(100):
   piarray.append(PiMC_v(1e6))
print("mean pi estimate:", np.mean(piarray))
print("estimated uncertainty:", np.std(piarray))

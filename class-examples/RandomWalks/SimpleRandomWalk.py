
# Code to carry out a simple one dimensional random walk and plot the path.
#
# Rob Owen, ph290, Oberlin College, Spring 2023.

import numpy as np 
import matplotlib.pyplot as plt

Nsteps = 100
x = 0 # We'll treat the position, x, as an integer.

# xlist = [x]
# for i in range(Nsteps):
#     r = np.random.randint(0,2) # Gives a random integer, zero or one.
#                                # Note, the first limit is inclusive,
#                                # the second is not.
#     x += (-1)**r # If r==0 go right, if r==1 go left.
#     xlist.append(x) #Append the current value of x, for plotting.

## A vectorized way to do the same thing:
# steptypes = np.random.randint(0,2,Nsteps)
# steps = (-1)**steptypes # change 0's and 1's into -'s and +'s
# xlist = np.cumsum(steps) # a "cumulative sum" function
# # But the previous way I did this we included the initial position, 0.
# # I can add that in with an append:
# xlist = np.append([0], xlist)

## The above can be combined into a single line (at the cost of some
## code readability).
xlist = np.append([0], np.cumsum((-1)**np.random.randint(0,2,Nsteps)))

#Print the final location to the screen:
print('Final location =', xlist[-1])

#Plot the path:
plt.axis([-50,50,0,100])
plt.title("Simple Random Walk")
plt.xlabel("location")
plt.ylabel('step number')
plt.plot(xlist, range(Nsteps+1), linewidth = 1, marker = "|")
plt.show()

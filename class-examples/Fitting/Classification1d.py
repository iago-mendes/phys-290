
# This code carries out "logistic regression" (that is, nonlinear fitting
# to the "logistic function") to show classification of true-false results 
# as related to a single independent variable.
# 
# Rob Owen, ph290, Oberlin College, Spring 2023

import numpy as np
import matplotlib.pyplot as plt


####################################################################
# Generating fake data for later analysis:
####################################################################

npoints = 100
# Random values of the independent variable, x:
x = np.random.uniform(0,1,npoints)

# The "true" parameters describing how the probability of a "true" value 
# depends on the independent variable "x":
alpha = -5.
k = 10.

# The logistic function, describing that probability:
def p(x, alpha, k):
    return 1./(1.+np.exp(-(alpha + k*x)))

# Now, we create an array "y", whose elements are all either zero or one, with 
# probability depending on the corresponding "x" as given by the logistic 
# function above.
# 
# The best technique I came up with for this involves two steps. At each x, we 
# choose a uniformly-distributed random number r, and then mark y to be 1 only 
# if r is less than the number given by the logistic function. Thus, the 
# probability of y being 1 is given by that logistic function.
r = np.random.uniform(0,1,npoints)
y = np.zeros_like(r)
for i in range(npoints): 
    if r[i]<p(x[i],alpha,k): y[i] = 1

# Plot the points:
plt.plot(x,y, lw=0, marker='o', color='r')
plt.ylim(-.5,1.5) # set the vertical scaling, so the points aren't cut off.
plt.show()

###########################################################
# Logistic Regression:
###########################################################

# Define the function that we want to minimize. 
# I'll be using a "packaged" minimization from scipy. This function wants 
# the function that we're minimizing to only have one argument, so we 
# package our two unknown quantities, alpha and k, into a "tuple" 
# called "params":
def MinusLogLikelihood(params):
    alpha, k = params
    v = k*np.mean(y*x) + alpha*np.mean(y) - np.mean(np.log(np.ones_like(x) + np.exp(alpha*np.ones_like(x)+k*x)))
    return -v

# Now, just let scipy's fmin function handle the minimization:
from scipy.optimize import fmin
print("minimizing penalty function")
params = fmin(MinusLogLikelihood, (-6.,6.)) # The (-6,6) is an initial guess.
print("[alpha, k] =", params)

#########################################################
# Output:
#########################################################

alph_computed, k_computed = params
print("  Transition point: x =", -alph_computed/k_computed)
print("  Width of transition: delta x =", 1./k_computed)
xfine = np.linspace(0.,1.,200)
plt.plot(xfine, p(xfine, alph_computed, k_computed))
plt.plot(x,y, lw=0, marker="o", color='r')
plt.ylim(-.5,1.5)
plt.show()

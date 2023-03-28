
# This code carries out "logistic regression" (that is, nonlinear fitting
# to the "logistic function") to show classification of true-false results 
# as related to a TWO independent variables.
#
# The structure of the code is identical to Classification1d, just in a higher 
# number of dimensions. This code is an example of a "linear classifier", 
# in the language of machine learning, in that it will try to sort datapoints 
# into two groups, separated by a straight line (shown with contour lines 
# in the final plot).
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
y = np.random.uniform(0,1,npoints)

# The "true" parameters describing how the probability of a "true" value 
# depends on the independent variable "x":
alpha = -10.
kx = 10.
ky = 10.

# The logistic function, describing that probability. Note that it now 
# depends on two independent coordinate values, x and y, and three parameters,
# alpha, kx, ky:
def p(x, y, alpha, kx, ky):
    return 1./(1.+np.exp(-(alpha + kx*x + ky*y)))

# Now, we create an array "z", whose elements are all either zero or one, with 
# probability depending on the corresponding "(x,y)" as given by the logistic 
# function above.
# 
# The best technique I came up with for this involves two steps. At each (x,y), 
# we choose a uniformly-distributed random number r, and then mark z to be 1 
# only if r is less than the number given by the logistic function. Thus, the 
# probability of z being 1 is given by that logistic function.
r = np.random.uniform(0,1,npoints)
z = np.zeros_like(r)
for i in range(npoints): 
    if r[i]<p(x[i],y[i],alpha,kx,ky): z[i] = 1

# The following three lines will draw a contour plot of the "true" probability,
# overlaid with the fake data representing this probability distribution. But 
# for now I'm leaving it commented out to better see things with the eye.
#X,Y = np.meshgrid(np.arange(0.,1.,.01),np.arange(0.,1.,.01))
#contplot = plt.contour(X,Y,p(X,Y,alpha,kx,ky), 20)
#plt.clabel(contplot)

# Now we plot our fake data. Note how I use conditional slices to find just 
# the subsets of x and y for which z equals 0 or 1, to plot them with different 
# colors and markers:
plt.plot(x[z>.5],y[z>.5], lw=0, marker='^', color='r')
plt.plot(x[z<.5],y[z<.5], lw=0, marker='o', color='b')
plt.show()


###########################################################
# Logistic Regression (linear classification):
###########################################################

# Define the function that we want to minimize. 
# I'll be using a "packaged" minimization from scipy. This function wants 
# the function that we're minimizing to only have one argument, so we 
# package our three unknown quantities, alpha, kx, ky, into a "tuple" 
# called "params":
def MinusLogLikelihood(params):
    alpha, kx, ky = params
    v = kx*np.mean(z*x) + ky*np.mean(z*y) + alpha*np.mean(z) - np.mean(np.log(np.ones_like(x) + np.exp(alpha*np.ones_like(x)+kx*x+ky*y)))
    return -v

# Now, just let scipy's fmin function handle the minimization:
from scipy.optimize import fmin
print("minimizing penalty function")
params = fmin(MinusLogLikelihood, (-6.,6.,6.))
print("[alpha, kx, ky] =", params)

#########################################################
# Output:
#########################################################

# First, we draw a contour plot of the inferred distribution:
X,Y = np.meshgrid(np.arange(0.,1.,.01),np.arange(0.,1.,.01))
alph_computed, kx_computed, ky_computed = params
contplot2 = plt.contour(X,Y,p(X,Y,alph_computed,kx_computed,ky_computed),20)
plt.clabel(contplot2)
# Then, we replot the data, on the same graph:
plt.plot(x[z>.5],y[z>.5], lw=0, marker='^', color='r')
plt.plot(x[z<.5],y[z<.5], lw=0, marker='o', color='b')
plt.show()


# This code carries linear least-squares fitting to a high-order 
# polynomial, showing overfitting (fitting to the noise), and the 
# benefits that can be gained by "regularizing" (that is, penalizing 
# each parameter in the minimization problem, to ask that they be made 
# small if consistent with the data.
#
# Rob Owen, ph290, Oberlin College, Spring 2023

import numpy as np
import matplotlib.pyplot as plt

# Start with evenly spaced values of the independent variable, x, and 
# make some fake data corresponding to y = x**3 + noise
x = np.arange(0.,5.,.25)
y = x**3 + np.random.normal(0.,10.,len(x))

# Simple scatter plot:
plt.plot(x, y, marker='o', lw=0)
plt.show()

# Basis functions for fit:
def f(x, alpha):
    return x**alpha

nparams = 10 # allow up to 10'th order polynomial fitting

# The matrix and vector needed for linear LSF:
M = np.zeros((nparams,nparams))
v = np.zeros(nparams)
# Note that I've started out by defining them as just a bunch of zeros. 
# Now I'll pack them with the real values:
for alpha in range(nparams):
    for beta in range(nparams):
        M[alpha,beta] = np.mean(f(x,alpha)*f(x,beta))
    v[alpha] = np.mean(y*f(x,alpha))

# Solve for the parameters in front of the basis functions:
theta = np.linalg.solve(M,v)
print("(over)fit coefficients:", theta)

# Construct a finely-spaced set of x-values, to construct a smooth plot 
# of the fitted curve:
xfine = np.linspace(0.,5.,300)
fittedcurve = np.zeros_like(xfine)
# Started with zero. Add in each theta times corresponding basis function:
for alpha in range(nparams):
    fittedcurve += theta[alpha]*f(xfine,alpha)

# Plot original points, and fitted curve. ("Overfitted" curve, that is.)
plt.plot(x, y, marker='o', lw=0)
plt.plot(xfine, fittedcurve)
plt.show()


# Now, start over but with "regularized" regression. Regularization means 
# adding terms of the form lambda[alpha]*theta[alpha]**2 to the residual that 
# we want to minimize. After the minimization problem, we get a similar matrix 
# problem, but the matrix has larger values on the diagonal:
lambd = 10. #Note that "lambda" is a protected word in python, so we can't use it.
for alpha in range(nparams):
    M[alpha,alpha] += lambd

theta = np.linalg.solve(M,v)
print("regularized fit coefficients:", theta)

# Plot the result, as before:
xfine = np.linspace(0.,5.,300)
fittedcurve = np.zeros_like(xfine)
for alpha in range(nparams):
    fittedcurve += theta[alpha]*f(xfine,alpha)

plt.plot(x, y, marker='o', lw=0)
plt.plot(xfine, fittedcurve, label="regularized LSF")
plt.plot(xfine, xfine**3, label="\'true\' dependence")
plt.legend()
plt.show()

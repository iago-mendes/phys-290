
# This code fits fake sinusoidal data to a general function, in a least-squares 
# sense. Because the model depends nonlinearly on the parameters 
# a nonlinear optimization scheme must be used. For rapid convergence, 
# one could use Newton-Raphson on the functions given by the partial 
# derivatives of chi-squared with respect to parameters. But here, we use a 
# simpler technique, called "gradient descent." We calculate explicitly 
# the derivatives of chi-squared with respect to a and b, and we use this 
# information to "step downhill" in the surface plot of chi-squared. This 
# technique is less efficient, but quite robust and comprehensible.
#
# The code, in this case, is written to accept a relatively general 
# model function, and as a result, does not use explicitly calculated 
# partial derivatives of chi-squared. Instead, it estimates the gradient of 
# chi-squared using finite differences.
#
# Rob Owen, physics 290, Oberlin College, Spring 2023


import numpy as np
import matplotlib.pyplot as plt


#Function defining our model:
def Model(x, a, b):
    return a*x**b

#First, we'll produce some fake data.
x = np.linspace(1., 30., 50) #50 evenly spaced measurements.

A, B = 1., -1. #"True" values of the parameters.
y = Model(x, A, B)   #This data exactly fits the model.
y = y + np.random.normal(0., .1, 50)
    # Now each y will have some gaussian-distributed random error.

# Show the data:
plt.scatter(x, y)
plt.show()



# The statistically-relevant measure of the mismatch 
# of a given dataset with the model is itself a function of the model 
# parameters a and b. Specifically:
def ChiSquared(a, b):
    return .5*np.mean((y-Model(x, a, b))**2)

# The above function implicitly assumes the parameters a and b are individual 
# numbers, not arrays (array multiplication of b*x wouldn't make sense if 
# b and x are arrays of different size). But below, we'd like to plot the 
# ChiSquared function for many values of a and b. Numpy's vectorize function 
# will handle the necessary bookkeeping for this.
ChiSquaredV = np.vectorize(ChiSquared)

# To do the gradient-descent for minimizing ChiSquared, we'll need to know
# the derivatives of ChiSquared with respect to a and b.
# Because we're handling general functions here, rather than specific functions
# where I'd be able to calculate these derivatives by hand, here I'm 
# approximating the derivatives using "finite difference" formulae:
def partial_a_ChiSquared(a, b):
    Delta_a = 1.e-6
    return (ChiSquared(a+Delta_a, b) - ChiSquared(a - Delta_a, b))/(2.*Delta_a)

def partial_b_ChiSquared(a, b):
    Delta_b = 1.e-6
    return (ChiSquared(a, b+Delta_b) - ChiSquared(a, b-Delta_b))/(2.*Delta_b)

# Visualizing the mismatch, as a function of model parameters:
ai = np.linspace(0., 2., 200)
bi = np.linspace(-2., 2., 200)
Ai,Bi = np.meshgrid(ai,bi)
Z = np.log(ChiSquaredV(Ai,Bi))

#plot a countour map of the dependence on model parameters
contplot = plt.contour(Ai,Bi,Z, 20)
plt.xlabel("a parameter")
plt.ylabel("b parameter")
plt.clabel(contplot)
plt.show()

#Optimization problem --- 
#Start with initial guess:
a = 2.
b = 1.

#We're gonna put pyplot into "interactive mode," which allows us to 
#animate the plot as the computation goes along.
plt.ion()
#For plotting curve during optimization:
plt.xlim(0.,32.)
plt.ylim(np.min(y)-1., np.max(y)+1.)
data, = plt.plot(x, y, marker='o', linewidth=0)
xfine = np.linspace(0.01,30., 100)
curve, = plt.plot(xfine, Model(xfine, a, b))
plt.draw()

#For plotting chi**2 during optimization:
#plt.contour(Ai,Bi,Z, 20)
#plt.colorbar()
#point, = plt.plot(a, b, marker = 'o')
input("Press enter to start movie...")
for i in range(3000):
    da = -partial_a_ChiSquared(a, b)
    db = -partial_b_ChiSquared(a, b)

    print(da, db)

    #check for huge gradients:
    norm = np.sqrt(da**2+db**2) + 1.e-5
    if norm>.1: 
        da = da/norm
        db = .1*db/norm

    a += da
    b += db

    print("a =", a, " b =", b)
    print("rms error =", np.sqrt(ChiSquared(a, b)))
    curve.set_ydata(Model(xfine, a, b))
    #point.set_xdata(a)
    #point.set_ydata(b)
    plt.draw()
    plt.pause(.01)
    if np.sqrt(da**2+db**2)<1.e-5: break
plt.ioff()

plt.plot(xfine, Model(xfine, a, b))
plt.plot(xfine, Model(xfine, A, B))
plt.scatter(x, y)
plt.show()



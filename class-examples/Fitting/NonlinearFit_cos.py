
# This code fits fake sinusoidal data to a sinusoid, in a least-squares 
# sense. Because the model, a*cos(b*x), depends nonlinearly on the parameter 
# b, a nonlinear optimization scheme must be used. For rapid convergence, 
# one could use Newton-Raphson on the functions given by the partial 
# derivatives of chi-squared with respect to a and b. But here, we use a 
# simpler technique, called "gradient descent." We calculate explicitly 
# the derivatives of chi-squared with respect to a and b, and we use this 
# information to "step downhill" in the surface plot of chi-squared. This 
# technique is less efficient, but quite robust and comprehensible.
#
# Rob Owen, physics 290, Oberlin College, Spring 2023


import numpy as np
import matplotlib.pyplot as plt


#First, we'll produce some fake data.
x = np.linspace(0., 30., 50) #50 evenly spaced measurements.

A, B = 1., 1. #"True" values of the parameters.
y = A*np.cos(B*x)   #This data exactly fits the model.
y = y + np.random.normal(0., .3, 50)
    # Now each y will have some gaussian-distributed random error.

# Show the data:
plt.scatter(x, y)
plt.show()



# We're gonna assume the "correct" model is f(x) = a*cos(b*x), for some 
# parameters a and b. The statistically-relevant measure of the mismatch 
# of a given dataset with this model is itself a function of the model 
# parameters a and b. Specifically:
def ChiSquared(a, b):
    return .5*np.mean((y-a*np.cos(b*x))**2)

# The above function implicitly assumes the parameters a and b are individual 
# numbers, not arrays (array multiplication of b*x wouldn't make sense if 
# b and x are arrays of different size). But below, we'd like to plot the 
# ChiSquared function for many values of a and b. Numpy's vectorize function 
# will handle the necessary bookkeeping for this.
ChiSquaredV = np.vectorize(ChiSquared)

# To do the gradient-descent for minimizing ChiSquared, we'll need to know
# the derivatives of ChiSquared with respect to a and b:
def partial_a_ChiSquared(a, b):
    return a*np.mean(np.cos(b*x)**2) - np.mean(y*np.cos(b*x))

def partial_b_ChiSquared(a, b):
    return -a*a*np.mean(x*np.cos(b*x)*np.sin(b*x)) + a*np.mean(y*x*np.sin(b*x))

# The fit of the model depends on the parameters a, and b. Let's visualize 
# this function using a contour plot:
ai = np.linspace(0., 3., 200)
bi = np.linspace(0., 5., 200)
Ai,Bi = np.meshgrid(ai,bi)
Z = ChiSquaredV(Ai,Bi)

# Drawing the contour plot:
contplot = plt.contour(Ai,Bi,Z, 20)
plt.xlabel("a parameter")
plt.ylabel("b parameter")
plt.clabel(contplot)
plt.show()



#Now, the optimization problem --- 
#Start with initial guess:
a = 1.1
b = 2.1

#We're gonna put pyplot into "interactive mode," which allows us to 
#animate the plot as the computation goes along.
plt.ion()
plt.xlim(0.,32.)
plt.ylim(-5., 5.)
data, = plt.plot(x, y, marker='o', linewidth=0)
xfine = np.linspace(0.,30., 100)
curve, = plt.plot(xfine, a*np.cos(b*xfine))
plt.draw()

#For plotting parameters on chi**2 contour map during optimization:
#plt.contour(Ai,Bi,Z2, 20)
#plt.colorbar()
#point, = plt.plot(a, b, marker = 'o')

input("Press enter to start movie...")
for i in range(500):
    da = -.01*partial_a_ChiSquared(a, b)
    db = -.01*partial_b_ChiSquared(a, b)

    print(da, db)

    #check for huge gradients:
    norm = np.sqrt(da**2+db**2)
    if norm>.1: 
        da = .01*da/norm
        db = .01*db/norm

    a += da
    b += db

    print("a =", a, " b =", b)
    print("rms error =", np.sqrt(ChiSquared(a, b)))
    curve.set_ydata(a*np.cos(b*xfine))
    #point.set_xdata(a)
    #point.set_ydata(b)
    plt.draw()
    plt.pause(0.01)
    if np.sqrt(da**2+db**2)<1.e-10: break
plt.ioff()

plt.plot(xfine, a*np.cos(b*xfine))
plt.plot(xfine, A*np.cos(B*xfine))
plt.scatter(x, y)
plt.show()




import numpy as np
import matplotlib.pyplot as plt

# Number of grid points:
N = 1001

# Define the grid and spacing:
x = np.linspace(0., 10., N)
# h = x[1] - x[0]
h = (x[-1] - x[0]) / (N-1)

print("grid spacing:", h)

# Some functions to serve as finite-difference operators
def ForwardDifference(F):
    Fprime = (np.roll(F, -1) - F)/h
    # Can't use forward-differencing at endpoint, so backward-diff there:
    Fprime[-1] = (F[-1] - F[-2])/h
    return Fprime

def BackwardDifference(F):
    Fprime = (F - np.roll(F, 1))/h
    # Can't use backward-diff at start point, so forward-diff there:
    Fprime[0] = (F[1] - F[0])/h
    return Fprime

def CenteredDifference(F):
    Fprime = (np.roll(F, -1) - np.roll(F, 1))/(2*h)
    # Can't use centered-differencing at either endpoint, so use one-sided:
    Fprime[0] = (F[1] - F[0])/h
    Fprime[-1] = (F[-1] - F[-2])/h
    return Fprime

def CenteredDifference2(F):
    Fprime = (np.roll(F, -1) - np.roll(F, 1))/(2*h)
    # Can't use centered-differencing at either endpoint, so use one-sided.
    # But the one-sided derivatives we used before were only first-order
    # accurate. Second-order accurate one sided derivatives are:
    Fprime[0] = (-F[2] + 4*F[1] - 3*F[0])/(2*h)
    Fprime[-1] = (3*F[-1] - 4*F[-2] + F[-3])/(2*h)
    return Fprime

# Define a function and its actual derivative, for testing:
#F = x**2
#FprimeAnalytical = 2.*x
F = np.sin(x)
FprimeAnalytical = np.cos(x)

FprimeFD = ForwardDifference(F)
FprimeBD = BackwardDifference(F)
FprimeCD = CenteredDifference2(F)

# Plot the true derivative and the FD approximation:
plt.plot(x, FprimeAnalytical)
plt.plot(x, FprimeFD, label='FD')
plt.plot(x, FprimeBD, label='BD')
plt.plot(x, FprimeCD, label='CD')
plt.legend()
plt.show()

# Plot the error in a few methods:
plt.plot(x, FprimeFD - FprimeAnalytical, label='FD')
plt.plot(x, FprimeBD - FprimeAnalytical, label='BD')
plt.plot(x, FprimeCD - FprimeAnalytical, label='CD')
plt.legend()
plt.show()

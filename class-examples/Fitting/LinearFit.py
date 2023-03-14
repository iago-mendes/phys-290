
# This code creates some "fake data" by taking linear data and adding 
# random error to it. It then fits a line to that fake data and plots 
# the data, the "true" relationship, and the fitted line.
#
# Rob Owen, physics 290, Oberlin College, Spring 2023

import numpy as np
import matplotlib.pyplot as plt


#First, we'll produce some fake data.
x = np.arange(0., 10., .5) #20 evenly spaced measurements.

A, B = 2., -5. #"True" values of the parameters.
y = A*x + B   #This data exactly fits the model.
y = y + np.random.normal(0., 3., 20)
    # Now each y will have some gaussian-distributed random error.

# Show the data:
plt.scatter(x, y)
plt.show()



# Now that we have a dataset, encoded in the arrays x and y, 
# we can construct the matrix M and the vector V for this dataset.

M = np.array([[np.mean(x**2), np.mean(x)],
              [np.mean(x), 1.]])

V = np.array([np.mean(y*x), np.mean(y)])

print("M =", M)
print("V =", V)

a, b = np.linalg.solve(M,V)
print('a =', a)
print('b =', b)

plt.plot(x, a*x + b, label="fitted line")
plt.plot(x, A*x+B, label="\'true\' dependence")
plt.scatter(x,y, label="randomized data")
plt.legend()
plt.show()


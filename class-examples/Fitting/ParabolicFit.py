
# This code produces "fake data" representing a parabolic relationship, 
# with random error. It then fits the data to a parabola and shows the results.
#
# Rob Owen, physics 290, Oberlin College, Spring 2023

import numpy as np
import matplotlib.pyplot as plt


#First, we'll produce some fake data.
x = np.arange(0., 10., .5) #20 evenly spaced measurements.

A, B, C = .5, -2., 3. #"True" values of the parameters.
y = A*x**2 + B*x + C  #This data exactly fits the model.
y = y + np.random.normal(0., 2., 20)
    # Now each y will have some gaussian-distributed random error.

# Show the data:
plt.scatter(x, y)
plt.show()



# Now that we have a dataset, encoded in the arrays x and y, 
# we can construct the matrix M and the vector V for this dataset.

M = np.array([[np.mean(x**4), np.mean(x**3), np.mean(x**2)],
              [np.mean(x**3), np.mean(x**2), np.mean(x)],
              [np.mean(x**2), np.mean(x), 1.]])

V = np.array([np.mean(y*x**2), np.mean(y*x), np.mean(y)])

print("M =", M)
print("V =", V)

a, b, c = np.linalg.solve(M,V)
print('a =', a)
print('b =', b)
print('c =', c)

chisquared = np.mean((y - a*x**2-b*x-c)**2)
print('quality of fit =', chisquared)

plt.plot(x, a*x**2+b*x+c, label="fitted curve")
plt.plot(x, A*x**2+B*x+C, label="\'true\' dependence")
plt.scatter(x,y, label="data with random noise")
plt.legend()
plt.show()


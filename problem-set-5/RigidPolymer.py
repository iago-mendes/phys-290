import numpy as np
import matplotlib.pyplot as plt

nlinks = int(input('Number of links: '))
flexibility = float(input('Flexibility: '))

theta_relative = np.random.normal(0., flexibility, nlinks)
theta_absolute = np.cumsum(theta_relative)
x = np.cumsum(np.cos(theta_absolute))
y = np.cumsum(np.sin(theta_absolute))

square_half_side = np.max(np.append(np.abs(x), np.abs(y))) * 1.05

plt.plot(x, y)

plt.xlim(-square_half_side, square_half_side)
plt.ylim(-square_half_side, square_half_side)

plt.xlabel('x')
plt.xlabel('y')
plt.title(f'Polymer with {nlinks} links of flexibility {flexibility}')

plt.show()

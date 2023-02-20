import numpy as np
import matplotlib.pyplot as plt
from cmath import phase

x1d = np.linspace(-2, 2, 1000)
y1d = np.linspace(-2, 2, 1000)
x, y = np.meshgrid(x1d, y1d)
z = x + 1j*y

for i in range(20):
	z = 2/3 * z + 1/3/z**2

z = np.vectorize(phase)(z)

print(z)

plt.imshow(z, extent=(-2,2,-2,2))
plt.scatter([1], [0], label=r'$(1,0)$', color="black")
plt.scatter([-1/2], [np.sqrt(3)/2], label=r'$\left(-\frac{1}{2},\frac{\sqrt{3}}{2}\right)$', color="orange")
plt.scatter([-1/2], [-np.sqrt(3)/2], label=r'$\left(-\frac{1}{2},-\frac{\sqrt{3}}{2}\right)$', color="red")
plt.xlabel(r'$Re(z)$')
plt.ylabel(r'$Im(z)$')
plt.legend()
plt.show()

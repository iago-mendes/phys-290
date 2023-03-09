import numpy as np
import matplotlib.pyplot as plt

# Part a

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
plt.ylabel('y')
plt.title(f'Polymer with {nlinks} links of flexibility {flexibility}')

plt.show()

# Part b

print('Computing typical sizes...')

nlinks = 1000

def PolymerSpan(flexibility):
	theta_relative = np.random.normal(0., flexibility, nlinks)
	theta_absolute = np.cumsum(theta_relative)
	x = np.cumsum(np.cos(theta_absolute))
	y = np.cumsum(np.sin(theta_absolute))

	d = np.sqrt((x[-1] - x[0])**2 + (y[-1] - y[0])**2)
	return d

def PolymerTypicalSize(flexibility):
	sizes = np.array([])

	for i in range(1000):
		sizes = np.append(sizes, PolymerSpan(flexibility))
	
	return np.average(sizes)

flexibilities = np.linspace(0.01, 2. * np.pi, 100)

typical_sizes = np.array([])
for flexibility in flexibilities:
	typical_sizes = np.append(typical_sizes, PolymerTypicalSize(flexibility))

plt.plot(flexibilities, typical_sizes, marker='o')

plt.xlabel('Flexibility')
plt.ylabel('Size')
plt.title('Typical sizes for polymer with various levels of flexibility')

plt.show()

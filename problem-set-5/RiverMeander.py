import numpy as np
import matplotlib.pyplot as plt

nsteps = 40
b = 10
theta0 = 110*np.pi/180
sigma = 17*np.pi/180

patharray_x = np.zeros((0, nsteps))
patharray_y = np.zeros((0, nsteps))

for i in range(int(1e6)):
	if (i % 1000 == 0):
		print('trial', i)
	
	theta_relative = np.random.normal(0., sigma, nsteps)
	theta_abs = np.cumsum(theta_relative)
	theta_abs = theta0 - theta_abs[0] + theta_abs
	x = np.cumsum(np.cos(theta_abs))
	y = np.cumsum(np.sin(theta_abs))

	if(np.sqrt((x[-1] - b)**2+(y[-1] - 0)**2) < 1):
		patharray_x = np.vstack([patharray_x, x])
		patharray_y = np.vstack([patharray_y, y])

npaths, ns = np.shape(patharray_x)
print(f'Found {npaths} paths')

meanx = np.mean(patharray_x, axis=0)
meany = np.mean(patharray_y, axis=0)

# Plot target region
target_x = np.linspace(b-1, b+1, 100)
target_y1 = np.sqrt(1 - (target_x - b)**2)
target_y2 = -np.sqrt(1 - (target_x - b)**2)
plt.plot(target_x, target_y1, lw=.5, color='black', label='Target region')
plt.plot(target_x, target_y2, lw=.5, color='black')

for i in range(npaths):
	plt.plot(patharray_x[i,:], patharray_y[i,:], lw=.1, color='blue')
plt.plot(meanx, meany, color='purple', label='Average path')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Model of a river meander')

plt.legend()
plt.show()

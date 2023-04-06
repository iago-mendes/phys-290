import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

############################
# Define parameters
############################

ngroups = 50
niterations = 10
# imfile = "Icebergs.jpg"
imfile = "Iago.jpg"

############################
# Read image
############################

Im = imread(imfile)
Ny, Nx, Nchannels = np.shape(Im)

points_r = Im[:,:,0]
points_g = Im[:,:,1]
points_b = Im[:,:,2]
npoints = np.size(points_r)
points_r = np.reshape(points_r, npoints)
points_g = np.reshape(points_g, npoints)
points_b = np.reshape(points_b, npoints)

############################
# K-means clustering
############################
print('Running k-means clustering...')

means_r = np.random.uniform(0,255,ngroups)
means_g = np.random.uniform(0,255,ngroups)
means_b = np.random.uniform(0,255,ngroups)

assignments = np.zeros_like(points_r, dtype="int")

def dist(r,g,b,mr,mg,mb):
	return np.sqrt((r-mr)**2+(g-mg)**2+(b-mb)**2)

distances = np.zeros((npoints,ngroups))

for i in range(niterations):
	for alpha in range(ngroups):
		distances[:,alpha] = dist(points_r, points_g, points_b, means_r[alpha], means_g[alpha], means_b[alpha])
	
	# Re-assign clusters
	assignments = np.argmin(distances, axis=1)

	# Averaging step:
	for alpha in range(ngroups):
		if len(points_r[assignments==alpha])==0:
			movetopoint = np.random.randint(0,npoints)
			means_r[alpha] = points_r[movetopoint]
			means_g[alpha] = points_g[movetopoint]
			means_b[alpha] = points_b[movetopoint]
		else:
			means_r[alpha] = np.mean(points_r[assignments==alpha])
			means_g[alpha] = np.mean(points_g[assignments==alpha])
			means_b[alpha] = np.mean(points_b[assignments==alpha])
	
	print(f'\t{(i+1)/niterations*100.:.2f}% complete')

############################
# RGB space
############################
print('Constructing RGB space...')

cpixels_r = np.zeros_like(points_r)
cpixels_g = np.zeros_like(points_g)
cpixels_b = np.zeros_like(points_b)

for i in range(npoints):
	cpixels_r[i]=means_r[assignments[i]]
	cpixels_g[i]=means_g[assignments[i]]
	cpixels_b[i]=means_b[assignments[i]]

cpixels = np.column_stack((cpixels_r, cpixels_g, cpixels_b))

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(points_r[::1000], points_g[::1000], points_b[::1000], c=cpixels[::1000]/255.)
ax.scatter(means_r, means_g, means_b, color='black', s=500, marker='+')
ax.set_xlabel('red')
ax.set_ylabel('green')
ax.set_zlabel('blue')
plt.show()

############################
# Color wheel
############################
print('Constructing color wheel...')

delta_theta = 2.*np.pi/ngroups
ncwx = 500
ncwy = 500
ColorWheelIm = np.zeros((ncwy,ncwx,3), dtype=int)
for i in range(ncwx):
	for j in range(ncwy):
		theta = np.pi + np.arctan2(j-.5*ncwy, i-.5*ncwx)
		group = int(theta/delta_theta)
		if(group==ngroups): group = ngroups-1
		ColorWheelIm[j,i,0] = means_r[group]
		ColorWheelIm[j,i,1] = means_g[group]
		ColorWheelIm[j,i,2] = means_b[group]
plt.imshow(ColorWheelIm)
plt.show()

############################
# Re-construct image
############################
print('Re-constructing image...')

cpixels_r_Reshaped = cpixels_r.reshape((Ny,Nx))
cpixels_g_Reshaped = cpixels_g.reshape((Ny,Nx))
cpixels_b_Reshaped = cpixels_b.reshape((Ny,Nx))
ImC = np.zeros_like(Im, dtype='int')
ImC[:,:,0] = cpixels_r_Reshaped
ImC[:,:,1] = cpixels_g_Reshaped
ImC[:,:,2] = cpixels_b_Reshaped

plt.imshow(ImC)
plt.gcf().set_size_inches(3, 4)
plt.savefig(f'assets/{ngroups}.png', format='png')
plt.show()

print('\nDone!')

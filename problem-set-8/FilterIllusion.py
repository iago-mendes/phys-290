import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# Read in the images
EinsteinImage = imread('Einstein.png')
CurieImage = imread('Curie.png')[:,:,0]

# Get resolution
Ny, Nx = np.shape(EinsteinImage)
if ((Ny,Nx) != np.shape(CurieImage)):
	print('Error: images must have the same resolution.')
	exit()

# Get fourier transforms
EinsteinImage_f = np.fft.fft2(EinsteinImage)
CurieImage_f = np.fft.fft2(CurieImage)

# Define coordinates in the frequency domain
freqx = np.fft.fftfreq(Nx)
freqy = np.fft.fftfreq(Ny)
kx, ky = np.meshgrid(freqx, freqy)

# Logistic function
def LogisticFn(x, x0, w):
	return 1./(1.+np.exp(-(x-x0)/w))

# Magnitude of the wave vector k (rotation-symmetric measure of oscillations)
Kmag = np.sqrt(kx**2+ky**2)

# Cut off any frequencies below 5% of the maximum value in the image
cutoffvalue = .05*np.max(Kmag)
    
# Apply high-pass filter
EinsteinImage_f *= LogisticFn(Kmag, cutoffvalue, .01)

# Apply low-pass filter
CurieImage_f *= 1 - LogisticFn(Kmag, cutoffvalue, .01)

# Convert back to position-space
EinsteinFiltered = np.fft.ifft2(EinsteinImage_f).real
CurieFiltered = np.fft.ifft2(CurieImage_f).real

# Combine images
MergedImage = .5*(EinsteinFiltered + CurieFiltered)

# Show result
plt.imshow(MergedImage, cmap='gray')
plt.show()

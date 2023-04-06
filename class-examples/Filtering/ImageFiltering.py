
# This code reads an image, computes and shows its spatial (2-d) Fourier
# transform, applies a high-pass filter in the Fourier domain, and transforms
# back to the spatial domain to show the filtered image.
#
# Rob Owen, Physics 290, Oberlin College, Spring 2023



# Import packages and functions, including 'imread', which reads an image file
# into a numpy array:
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread


# Read in the image and find its resolution:
EinsteinImage = imread('Einstein.jpg')
Ny, Nx = np.shape(EinsteinImage)

# First, let's see the image we're working with:
plt.imshow(EinsteinImage, cmap='gray')
plt.show()

# fft2 is a function for two-dimensional fourier transforms:
EinsteinImage_f = np.fft.fft2(EinsteinImage)


# To apply a filter in fourier space, we need coordinates in the frequency
# domain. Numpy has a function for this, fftfreq, but it's only made for
# one dimension. I use meshgrid to expand it to our 2-d representation:
freqx = np.fft.fftfreq(Nx)
freqy = np.fft.fftfreq(Ny)

kx, ky = np.meshgrid(freqx, freqy)


# To view images in the fourier domain, we'll need a few helper functions:

# First, a normalization function that makes sure all pixel values
# range from 0 to 1:
def NormImage(Im):
    ImC = np.copy(Im)
    ImC -= np.min(Im)
    ImC /= np.max(Im)
    return ImC

# The following function corrects for the annoying fact that np.fft indexes
# the fourier-transformed data in an unexpected way:
def ImFftRoll(Im):
    ImC = np.copy(Im)
    N0, N1 = np.shape(Im)
    ImC = np.roll(ImC, int(N0/2), axis = 0)
    ImC = np.roll(ImC, int(N1/2), axis = 1)
    return ImC

# Finally, this function strings together the previous functions so that
# we only have to call this function to plot the fourier transform of an image:
def ShowImageTransform(Im):
    plt.imshow(ImFftRoll(NormImage(np.log(1+abs(Im.real)))), cmap='gray')
    plt.show()
    return

# So here's the FFT of the Einstein Image:
ShowImageTransform(EinsteinImage_f)
# Doesn't it look wise?


# For filtering, I need a smooth function that will interpolate between
# zero and one at some prescribed cutoff point x0. I'll do this with our
# friend the logistic function:
def LogisticFn(x, x0, w):
    return 1./(1.+np.exp(-(x-x0)/w))


# Let's filter the image according to a rotation-symmetric measure of
# oscillations: the magnitude of the wave vector k:
Kmag = np.sqrt(kx**2+ky**2)

# For a high-pass filter, I'll cut off any frequencies below 4% of the
# maximum value in the image:
cutoffvalue = .04*np.max(Kmag)

    
# To filter, I simply multiply by the cutoff function, in frequency space:
EinsteinImage_f *= LogisticFn(Kmag, cutoffvalue, .01)

# Let's see what that did to the FFT:
ShowImageTransform(EinsteinImage_f)

# Finally, convert back to position-space:
EinsteinFiltered = np.fft.ifft2(EinsteinImage_f).real

# And let's see what we've done:
plt.imshow(EinsteinFiltered, cmap='gray')
plt.show()

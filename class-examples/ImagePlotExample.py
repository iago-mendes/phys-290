
import numpy as np
import matplotlib.pyplot as plt



# The "image plot" is a convenient way to visualize data that might have two
# independent variables -- things like a function z = f(x, y). This kind of
# function can be visualized with a "surface plot" as well (which we'll talk
# about another day), but usually I find that image plots are clearer
# to read, because there aren't any issues of forced perspective.


# First, we need a grid of x and y points. For image plots, these are usually
# a uniform cartesian grid (I actually don't even know if it can be done with
# a non-uniform grid!). Pyplot likes the x and y coordinates to be in
# two-dimensional arrays, which you might visualize as matrices. For this
# reason, image plots are sometimes referred to as "matrix plots"
# (I actually often use them to visualize large matrices, when I want to see
# which elements are nonzero, but that's another story). To construct these
# 2-d arrays, we can start by defining two 1-d arrays:

x1d = np.linspace(-5., 5., 50)
y1d = np.linspace(-5., 5., 50)

# We can now turn these into two 2-d arrays using a convenient numpy function
# called "meshgrid":

x, y = np.meshgrid(x1d, y1d, indexing='xy')

# We can see what we have here by printing the x and y arrays, though because
# they're now both 50-by-50 matrices, only a small subset of the data will
# be shown:
print(x)
print(y)

# Note: the argument "indexing='xy'" is a workaround for an annoying
# inconsistency of notation. In conventional matrix notation, when referring
# to components of a matrix, the first index conventionally defines the "row"
# (that is, how far "down" the element is from the top), and the second index
# defines the "column" (how far "over" the element is from the left). In
# the world of computer visualization, this convention has historically been
# carried over to labeling pixels in an image. Unfortunately this is contrary
# to the usual convention for labeling points in cartesian axes, where the
# first coordinate is the horizontal coordinate and the second is the vertical.
# For many years, matplotlib and meshgrid defaulted to the "matrix index"
# based scheme (which can still be used, with the option "indexing='ij'").
# Now I think they've recently changed the default to 'xy', but I still
# include it to be sure.

# Now, we need to compute the corresponding z values for each point on this
# grid. To do that, we can simply apply a function. Again, numpy's functions
# are "vectorized," which means that you don't have to write an explicit loop
# over the grid points to calculate each z-value (though you could, if you
# needed to). 

# Actually, to start, let's just do a simple polynomial function. These only
# require algebraic operators, which numpy also vectorizes. Let's do a
# hyperboloid:

z = x**2 - y**2


# To create and display the plot, there's a simple function in pyplot called
# "imshow":

plt.imshow(z)
plt.show()



# This is nice, but there are some issues. Maybe the most obvious is that the
# axes aren't labeled by x and y values, but instead by matrix indices. This
# is because we didn't give the x and y arrays. You'd think the function would
# know what to do if you simply gave it those arrays as well, but sadly that
# doesn't seem to have been implemented yet. But we can override the axis labels
# by adding the "extent" argument, which takes the limits of the x and y axes
# and infers all point locations from that:

plt.imshow(z, extent=(-5, 5, -5, 5))
plt.show()



# That's an improvement, but another thing that would be useful is a "colorbar",
# which shows what numerical value each color corresponds to:

plt.imshow(z, extent=(-5, 5, -5, 5))
plt.colorbar()
plt.show()




# There's also a "pixelated" effect in the images we've shown above. This is
# because imshow draws everything as a discrete set of pixels, with discrete
# jumps in shading. To get a smoother picture, we can turn on interpolation:
plt.imshow(z, extent=(-5, 5, -5, 5), interpolation='bicubic')
plt.colorbar()
plt.show()




# Also, you might not like the default color pattern (blue to yellow in the
# defaults on the machine I'm currently using). If you'd like to change them,
# you could do that by changing the "colormap". Here's one called 'hot',
# inspired by thermal radiation.
plt.imshow(z, extent=(-5, 5, -5, 5), interpolation='bicubic', cmap='hot')
plt.colorbar()
plt.show()
# for a listing of standard colormaps, see here:
#   https://matplotlib.org/stable/gallery/color/colormap_reference.html
# You can actually make your own colormaps as well, though in my experience
# that's a slightly tedious process.





# Sometimes we aren't looking for a mapping from a 2-d space to a 1-d space
# (in other words, a colormap as used above). Sometimes we want the whole
# three-dimensional space of colors allowed by our RGB ("red-green-blue")
# color displays, which are in turn tuned to the three different varieties of
# "cone cells" that exist in most human retinas. To do that, on this 50-by-50
# grid, I can give a 50-by-50-by-3 array, with each "layer" of this array
# giving values for (respectively), red, green, and blue
r = (x**2 - y**2)
g = 2*x*y
b = .8*np.max(r)*(np.cos(3.*np.sqrt(x**2+y**2)))

# Now, pack these into the big 50-by-50-by-3 array:
pixelcolorings = np.zeros((50, 50, 3)) # defines an array of all zeros, which
                                       # I'll overwrite next.
pixelcolorings[:,:,0] = r
pixelcolorings[:,:,1] = g
pixelcolorings[:,:,2] = b

# Note, though, that all of these numbers need to be between zero and one.
# (This is for floats. If I was designating the colors in integers it'd
#  want them to range from 0 to 255. Eight bits.)
# Because I've hugely violated that in the above functions, I'll do some
# rescaling:
pixelcolorings -= np.min(pixelcolorings)
pixelcolorings *= 1./np.max(pixelcolorings)

plt.imshow(pixelcolorings, extent=(-5, 5, -5, 5), interpolation='bicubic')
plt.show()


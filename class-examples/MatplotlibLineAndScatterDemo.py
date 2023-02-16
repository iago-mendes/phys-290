

# First, the opening line of 95% of the codes I write:
import numpy as np
# The numpy package has precompiled and optimized functions for a variety of
# operations with "arrays" a very convenient data type for holding collections
# of many numbers. 


# Then, the second line of about 80% of the codes I write:
import matplotlib.pyplot as plt
# Pyplot is an interface to the standard python plotting system, matplotlib



# Let's start by graphing a curve. For this, pyplot will need x- and y-values
# for a collection of many data points. Often, especially for graphs, we use
# a uniform distribution of x-values (though this is by no means required):

x = np.linspace(0., 20, 500)
# numpy's "linspace" function is designed to split a domain into many uniformly
# spaced samples. In this case, it's taking the domain from x=0 to x=20, and
# subdividing it into 500 elements. To see what it does, we can print it to the
# screen:
print(x)
# Note that, by default, linspace includes both endpoints in the array
# (though this behavior can be changed by adding extra arguments to the
# linspace function).


# Let's say we want to plot two functions, sin(x) and cos(x). Numpy has
# "vectorized" mathematical functions that make this really easy:

y1 = np.cos(x)
y2 = np.sin(x)

# Both of these lines compute new arrays, also 500 elements each, but their
# values are the values of cos(x) and sin(x), element by element. Without numpy,
# x might be defined as a list, and computing the sine or cosine of each element
# would have to be done as a loop, which is SLOW. So numpy's vectorized
# functions are not only convenient, they're also much more computationally
# efficient, because the loop is precompiled as part of the interpreter, rather
# than a set of instructions that the interpreter needs to carry out.


# Now, if we want to plot one of these curves, we can use pyplot's function
# 'plot', which takes an array of x-values, an array of corresponding y-values,
# and places them in axes (with a default structure that can be modified
# heavily), and (by another changeable default), connects the points with
# line segments to give a smooth curve:

plt.plot(x, y1)
plt.xlabel("x") # (optional -- this labels the horizontal axis)
plt.ylabel("cos(x)") # (optional -- this labels the vertical axis)
plt.show() # (This constructs the plot and shows it in a popup window)
# Actually, I say it shows the plot in a popup window -- in reality it
# depends a bit on your environment. In ipython/jupyter the plot might
# show up "inline" in the document. If you're working in Spyder (and I
# presume a variety of python IDEs), it might send them to a dedicated
# panel in the IDE (though again, this behavior can be changed).
# In some environments, the plt.show() command isn't even necessary,
# but for portability purposes I always include it if I can. 


# Now let's plot two curves in the same graph. The easiest way to do this is
# with two separate plt.plot commands.
plt.plot(x, y1, label="cos(x)")
plt.plot(x, y2, label="sin(x)", linestyle="--", linewidth=3)
plt.xlabel("x")
plt.legend()
plt.show()



# Notice the "legend" business. Since we're plotting two curves, we can't just
# put the y-label on the y-axis as we did in the previous plot. The function
# "plt.legend()" puts a legend in the graph to label the curves. (The legend
# location is chosen automatically with the goal of minimally disrupting the
# graphs, though again, this can be overriden.) In order to create a legend,
# though, it needs to know how to label the curves, so that's why I added the
# "label" arguments to my two calls to plt.plot.

# Note also that for the y2 curve, I've modified the "linestyle" to make it
# dashed and the "linewidth" to make it a little thicker.






# Now, let's construct a "scatter plot", a graph with just discrete points.
# The x- and y-data might come from other calculations, from read-in data,
# or any number of sources. To keep it simple and just show the scatter plot
# functionality, I'll start with just arbitrarily typing in strings of numbers.

xscatter = [0., .5, 3, 4.2, 4.8, 5.5, 6.9, 7.5, 8.8, 9.9]
# I'm using the name "xscatter" rather than x because I want to reserve the
# x array from above for another demo further down.
# Note also: this is a *list*, not a numpy array. I could explicitly define
# it as an array by puttin the whole thing inside np.array( ... ), but
# that isn't necessary because pyplot knows to convert lists to numpy
# arrays when it needs to.

yscatter = [.6, .3, -.2, -.7, -.8, -.5, -.1, .3, .5, .8]

# I can plot these using the plt.scatter function:
plt.scatter(xscatter, yscatter)
plt.xlabel("x values")
plt.ylabel("corresponding y values")
plt.show()


# Note that, by default, it draws the points as blue circles (at least on the
# machine where I'm writing the code). This can be changed:
plt.scatter(xscatter, yscatter, color='g', marker='x', s = 70)
plt.xlabel("x values")
plt.ylabel("corresponding y values")
plt.show()
# The labels for the different marker options are sometimes opaque (x is rather
# obvious, but many are easy to forget). I often find myself googling
# "pyplot marker styles" to remember the options. When I did it just now
# I found this useful listing:
#   https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
# Finally, the option "s = (some number)" lets you change the sizes of the
# markers.


# Note: it's also possible to add markers to a line-plot (the plots up above),
# by defining a marker shape. You wouldn't want to do this if there are 500
# points, just because the picture would be messy, but if you want a scatter
# plot with line connectors this can be useful. You can even set the line width
# to zero, and also add point markers, which would allow you to make a scatter
# plot using plt.plot rather than plt.scatter. Ultimately, plt.scatter is just
# a modified form of plt.plot with defaults changed for use in scatter plots.



# Finally, note that you can add multiple data sets on the same graph. We
# already did this with line plots above, but you can mix in scatter plots
# as well:
plt.plot(x, y1, label="cos(x)", color='k', linestyle='dotted')
plt.plot(x, y2, label="sin(x)", linestyle="-.", linewidth=3)
plt.scatter(xscatter, yscatter, label="unrelated discrete data", color='orange', marker='*', s = 100)
plt.xlabel("x")
plt.legend()
plt.show()



# This is all just the tip of an extremely large iceberg. If you google
# "matplotlib examples" you'll find listings of many many examples that
# add things like shading, polar coordinate grids, nonuniform colors and sizes,
# modifications to the tick-mark structure, grids underneath the graphs, etc.

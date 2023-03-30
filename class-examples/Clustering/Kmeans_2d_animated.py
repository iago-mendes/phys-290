
# This code constructs some number of datapoints in two-dimensional space,
# and groups them into a given number of divisions using K-means clustering.
#
# Rob Owen, ph290, Oberlin College, Fall 2023

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


###################################################################
# Generate fake data:
###################################################################

npoints = 100 # number of data points

ngroups = 3
# We'll intentionally cluster the datapoints together into this many groups. 
# The algorithm will subdivide data even if it isn't clustered into groups, 
# but if you want to think of the algorithm as a sort of "pattern recognition", 
# then this is the kind of pattern that it'll naturally try to uncover.

# First, divide up our data points (npoints of them) into smaller sections, 
# each with nsec elements:
nsec = np.zeros(ngroups, dtype="int")
for i in range(ngroups): nsec[i] = npoints/ngroups
nsec[-1]+= npoints - np.sum(nsec)
# Note that each section alpha has its own nsec, but I've defined them in such 
# a way that they're nearly all equal (just laziness on my part).

# Now, choose random coordinate locations for the centers of these groups:
centers_x = np.random.uniform(0.,1.,ngroups)
centers_y = np.random.uniform(0.,1.,ngroups)

# Now, define coordinate locations for all the datapoints. Start with an 
# empty array:
points_x = np.array([])
points_y = np.array([])
# now, for each group, append nsec worth of data points, given by a
# gaussian ("normal") probability distribution:
for i in range(ngroups):
    points_x = np.append(points_x, np.random.normal(centers_x[i], .1, nsec[i]))
    points_y = np.append(points_y, np.random.normal(centers_y[i], .1, nsec[i]))

# Now, plot them in 2d space, using pyplot's scatter function:
plt.scatter(points_x, points_y)
plt.show()



############################################################################
# Now, do K-means clustering:
############################################################################

# First, start with random guesses for the centroids (ngroups of them):
means_x = np.random.uniform(0.,1.,ngroups)
means_y = np.random.uniform(0.,1.,ngroups)

# Now, define an array of integers, which will hold information about which 
# centroid each datapoint is assigned to:
assignments = np.zeros_like(points_x, dtype="int")

# A function defining the Euclidean distance between some datapoint location 
# given by (x,y), and a centroid location given by (mx,my):
def dist(x,y,mx,my):
    return np.sqrt((x-mx)**2+(y-my)**2)

# Define an array in which we'll pack the distance from each datapoint to each 
# centroid:
distances = np.zeros((npoints,ngroups))

for iter in range(10):  # The iterations of the K-means clustering algorithm.

    # Assignment step:
    # We need to calculate the distance from each datapoint (labeled i) to 
    # each centroid (labeled alpha).
    # The below construction is probably relatively straightforward to read, 
    # but it uses a loop within a loop, which can become slow in python when 
    # there are many data points and/or many groups. 
    # A "vectorized" version that avoids the explicit loops is implemented in 
    # Kmeans_3d.py, and that version is much faster. For the current purposes
    # I'll leave the more intuitive non-vectorized version:
    for i in range(npoints):
        for alpha in range(ngroups):
            distances[i,alpha] = dist(points_x[i],points_y[i],means_x[alpha],means_y[alpha])

    # Now, we "assign" each datapoint to the proper group by finding the alpha 
    # value (centroid number) that minimizes the distance to each data point.
    assignments = np.argmin(distances, axis=1)

    # And now, plot the results:
    # datapoints: color-coded by their current assignments:
    plt.scatter(points_x, points_y, c=assignments, cmap=cm.jet, linewidths=0)
    # The computed centroids:
    plt.scatter(means_x, means_y, color='k', s=500, marker='+')
    plt.show()


    # Averaging step:
    for alpha in range(ngroups):
        # First, if a group has no elements, then we can't take a mean. 
        # A hacky but effective workaround for this is to just move that 
        # centroid to a random datapoint in that case:
        if len(points_x[assignments==alpha])==0:
            movetopoint = np.random.randint(0,npoints)
            means_x[alpha] = points_x[movetopoint]
            means_y[alpha] = points_y[movetopoint]
        # If a centroid does have datapoints associated with it, move the 
        # centroid to the average of those datapoints:
        else:
            means_x[alpha] = np.mean(points_x[assignments==alpha])
            means_y[alpha] = np.mean(points_y[assignments==alpha])
            # Note how I've used a "conditional slice" to take the mean of 
            # only those points for which "assignments" equals alpha.





# And now, plot the results:
# datapoints: color-coded by their final assignments:
plt.scatter(points_x, points_y, c=assignments, cmap=cm.jet, linewidths=0)
# The computed centroids:
plt.scatter(means_x, means_y, color='k', s=500, marker='+')
# The original centroids from when we made up the data:
plt.scatter(centers_x, centers_y, color='k', s=500, marker='*')
plt.title("Stars: original centers; Pluses: reconstructed centers; Circles: sorted points\nPluses would only be expected to be close to stars if original clusters don't overlap.")
plt.show()





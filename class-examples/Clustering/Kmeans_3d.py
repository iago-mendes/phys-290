
# This code constructs some number of datapoints in three-dimensional space,
# and groups them into a given number of divisions using K-means clustering.
# 
# Rob Owen, ph290, Oberlin College, Fall 2023

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D


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
for alpha in range(ngroups): nsec[alpha] = npoints/ngroups
nsec[-1]+= npoints - np.sum(nsec)
# Note that each section alpha has its own nsec, but I've defined them in such 
# a way that they're nearly all equal (just laziness on my part).

# Now, choose random coordinate locations for the centers of these groups:
centers_x = np.random.uniform(0.,1.,ngroups)
centers_y = np.random.uniform(0.,1.,ngroups)
centers_z = np.random.uniform(0.,1.,ngroups)

# Now, define coordinate locations for all the datapoints. Start with an 
# empty array:
points_x = np.array([])
points_y = np.array([])
points_z = np.array([])
# now, for each group, append nsec worth of data points, given by a
# gaussian ("normal") probability distribution:
for alpha in range(ngroups):
    points_x = np.append(points_x, np.random.normal(centers_x[alpha], .1, nsec[alpha]))
    points_y = np.append(points_y, np.random.normal(centers_y[alpha], .1, nsec[alpha]))
    points_z = np.append(points_z, np.random.normal(centers_z[alpha], .1, nsec[alpha]))

# Now, plot them in 3d space, using mplot3d's three-dimensional scatter:
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(points_x, points_y, points_z)
plt.show()


############################################################################
# Now, do K-means clustering:
############################################################################

# First, start with random guesses for the centroids (ngroups of them):
means_x = np.random.uniform(0.,1.,ngroups)
means_y = np.random.uniform(0.,1.,ngroups)
means_z = np.random.uniform(0.,1.,ngroups)

# Now, define an array of integers, which will hold information about which 
# centroid each datapoint is assigned to:
assignments = np.zeros_like(points_x, dtype="int")

# A function defining the Euclidean distance between some datapoint location 
# given by (x,y,z), and a centroid location given by (mx,my,mz):
def dist(x,y,z,mx,my,mz):
    return np.sqrt((x-mx)**2+(y-my)**2+(z-mz)**2)

# Define an array in which we'll pack the distance from each datapoint to each 
# centroid:
distances = np.zeros((npoints,ngroups))

for iter in range(30): # The iterations of the K-means clustering algorithm.

    # Assignment step:
    # We need to calculate the distance from each datapoint (labeled i) to 
    # each centroid (labeled alpha). The following loop-within a loop is 
    # probably easy to read, but unfortunately gets slow if there's a lot of 
    # data or a lot of loops, so I've commented it out for now:
    #for i in range(npoints):
    #    for alpha in range(ngroups):
    #        distances[i,alpha] = dist(points_x[i],points_y[i],points_z[i],means_x[alpha],means_y[alpha],means_z[alpha])

    # Instead of a loop-within-a-loop, like in the three lines above, we use 
    # the magic of vectorized notation to do the same work in just a single 
    # loop. This is MUCH faster if there are a huge number of data points:
    for alpha in range(ngroups):
        distances[:,alpha] = dist(points_x, points_y, points_z, means_x[alpha], means_y[alpha], means_z[alpha])

    # Now, we "assign" each datapoint to the proper group by finding the alpha 
    # value (centroid number) that minimizes the distance to each data point.
    assignments = np.argmin(distances, axis=1)
    # The argmin function finds the index of an array with the minimum stored 
    # value (smallest distance, in this case). Note that the above line is 
    # again a vectorized calculation: "assignments" is an array with 'npoints' 
    # elements. We're handling each element simultaneously. Again, this could 
    # be done with a loop, but that would be slower.

    # Averaging step:
    for alpha in range(ngroups):
        # First, if a group has no elements, then we can't take a mean. 
        # A hacky but effective workaround for this is to just move that 
        # centroid to a random datapoint in that case:
        if len(points_x[assignments==alpha])==0:
            movetopoint = np.random.randint(0,npoints)
            means_x[alpha] = points_x[movetopoint]
            means_y[alpha] = points_y[movetopoint]
            means_z[alpha] = points_z[movetopoint]
        # If a centroid does have datapoints associated with it, move the 
        # centroid to the average of those datapoints:
        else:
            means_x[alpha] = np.mean(points_x[assignments==alpha])
            means_y[alpha] = np.mean(points_y[assignments==alpha])
            means_z[alpha] = np.mean(points_z[assignments==alpha])
            # Note how I've used a "conditional slice" to take the mean of 
            # only those points for which "assignments" equals alpha.


############################################################################
# Output:
############################################################################

# And now, just do a 3d plot:
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
# Plot the data points, color coded by assignment:
ax.scatter(points_x, points_y, points_z, c=assignments, cmap=cm.jet)
# Plot the centroids:
ax.scatter(means_x, means_y, means_z, color='k', s=500, marker='+')
plt.show()

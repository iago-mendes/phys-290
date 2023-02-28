import matplotlib.pyplot as plt

# This code defines two functions, the first applies von Neumann's 
# "Middle Square" technique to generate pseudo-random integers. The second 
# simply rescales these integers into uniformly-distributed random floats 
# between 0 and 1.
#
# Note that the results of these functions look good for a while, but after 
# about 16,000 iterations (I haven't counted carefully but it's somewhere 
# between 10k and 20k), the sequence "collapses."
#
# The code as I've written it only defines these functions. It doesn't call 
# them. You could add lines to this code to call the functions, or you could 
# read these functions into an interactive python shell with the command:
# exec(open("MiddleSquare.py").read())
# Note, however, that you might need to provide a full path to the file. 
#
# Rob Owen, ph290, Oberlin College, Spring 2023

seed = 1111111111

def MiddleSquare():
	global seed
	x = seed
	x = x*x

	x=x//int(1e5) # removes last 5 digits
	x=x%int(1e10) # removes first 5 digits

	seed = x
	return x

def MiddleSquareF():
	return float(MiddleSquare())/1.e10

randlist = []
for i in range(20000):
	randlist.append(MiddleSquare())

plt.hist(randlist, 20)
plt.show()

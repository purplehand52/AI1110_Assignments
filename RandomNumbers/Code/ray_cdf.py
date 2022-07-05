#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import theo_func as t

#Points on X-Axis
x = np.linspace(-4,4,30)

#Number of Samples
simlen = int(1e6)

#Probability Values
err = []

#Load Values (From Files)
randvar = np.loadtxt('ray.dat',dtype='double')

#Store Values
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

vec_ray_cdf = np.vectorize(t.ray_cdf, otypes=[float])

#Plot statistical values
plt.plot(x.T, err, 'ob')

#Plot theoretical values
plt.plot(x.T, vec_ray_cdf(x), '-g')

#Create Grid and Labels
plt.legend(["Numerical", "Theoretical"])
plt.grid()
plt.xlabel('$A$')
plt.ylabel('$F_A(a)$')

#Save Files
plt.savefig('../figs/ray_cdf.pdf')
plt.savefig('../figs/ray_cdf.png')

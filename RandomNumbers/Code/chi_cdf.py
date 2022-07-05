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
randvar = np.loadtxt('chi.dat',dtype='double')

#Store Values
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

vec_chi_cdf = np.vectorize(t.chi_cdf, otypes=[float])

#Plot statistical values
plt.plot(x.T, err, 'ob')

#Plot theoretical values
plt.plot(x.T, vec_chi_cdf(x), '-g')
#plt.plot(x.T, gau_val, '-g')
#plt.plot(x.T, log_val, '-g')

#Create Grid and Labels
plt.legend(["Numerical", "Theoretical"])
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#Save Files
plt.savefig('../figs/chi_cdf.pdf')
plt.savefig('../figs/chi_cdf.png')

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
#randvar = np.loadtxt('log.dat',dtype='double')

#Store Values
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
#Theoretical Stuff
#Function3: Log Distribution
def log_cdf(x):
    if(x < 0):
        return(0)
    else:
        return(1 - math.exp(-x/2))

vec_log_cdf = np.vectorize(t.log_cdf, otypes=[float])
log_val = vec_log_cdf(x)

#Plot statistical values
plt.plot(x.T, err, 'ob')

#Plot theoretical values
plt.plot(x.T, log_val, '-g')

#Create Grid and Labels
plt.legend(["Numerical", "Theoretical"])
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')

#Save Files
plt.savefig('../figs/log_cdf.pdf')
plt.savefig('../figs/log_cdf.png')

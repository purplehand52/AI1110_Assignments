#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import theo_func as t

#Points on X-Axis
x = np.linspace(-4,4,30)
x_new = np.linspace(-4,4,100)

#Number of Samples
simlen = int(1e6)

#Probability Values
err = []

#Load Values (From Files)
randvar = np.loadtxt('tri.dat',dtype='double')

#Store Values
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
#Theoretical Stuff
#Function4: Triangular Distribution 
def tri_cdf(x):
    if(x < 0):
        return(0)
    elif((x >= 0) and (x < 1)):
        return(x*x/2)
    elif((x >= 1) and (x < 2)):
        return(1 - (x-2)*(x-2)/2)
    else:
        return(1)

vec_tri_cdf = np.vectorize(t.tri_cdf, otypes=[float])
tri_val = vec_tri_cdf(x_new)

#Plot statistical values
plt.plot(x.T, err, 'ob')

#Plot theoretical values
plt.plot(x_new.T, tri_val, '-g')

#Create Grid and Labels
plt.legend(["Numerical", "Theoretical"])
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

#Save Files
plt.savefig('../figs/tri_cdf_comp.pdf')
plt.savefig('../figs/tri_cdf_comp.png')

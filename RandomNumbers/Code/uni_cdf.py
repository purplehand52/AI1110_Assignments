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
randvar = np.loadtxt('uni.dat',dtype='double')

#Store Values
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
#Theoretical Stuff
#Function1: Uniform Distribution
def uni_cdf(x):
    if(x < 0):
        return(0)
    elif(x > 1):
        return(1)
    else:
        return(x)

vec_uni_cdf = np.vectorize(t.uni_cdf, otypes=[float])
x_new = np.linspace(-4, 4, 150)
uni_val = vec_uni_cdf(x_new)

#Plot statistical values
plt.plot(x.T, err, 'ob')

#Plot theoretical values
plt.plot(x_new.T, uni_val, '-g')

#Plot Labels
plt.legend(["Numerical", "Theoretical"])
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_U(x)$')

#Save Files
plt.savefig('../figs/uni_cdf.pdf')
plt.savefig('../figs/uni_cdf.png')

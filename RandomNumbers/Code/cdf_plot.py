#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math

#Points on X-Axis
x = np.linspace(-4,4,30)

#Number of Samples
simlen = int(1e6)

#Probability Values
err = []

#Load Values (From Files)
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('log.dat',dtype='double')

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

vec_uni_cdf = np.vectorize(uni_cdf, otypes=[float])
uni_val = vec_uni_cdf(x)

#Function2: Gaussian Distribution
def gau_cdf(x):
    return((1/2) * (1 + math.erf(x/math.sqrt(2))))

vec_gau_cdf = np.vectorize(gau_cdf, otypes=[float])
gau_val = vec_gau_cdf(x)

#Function3: Log Distribution
def log_cdf(x):
    if(x < 0):
        return(0)
    else:
        return(1 - math.exp(-x/2))

vec_log_cdf = np.vectorize(log_cdf, otypes=[float])
log_val = vec_log_cdf(x)

#Print Values
#print(x)
#print(uni_val)
#print(gau_val)
#print(log_val)

#Plot statistical values
plt.plot(x.T, err, 'bo')

#Plot theoretical values
plt.plot(x.T, uni_val)
#plt.plot(x.T, gau_val)
#plt.plot(x.T, log_val)

#Create Grid and Labels
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')

#Save Files
plt.savefig('../figs/uni_cdf.pdf')
plt.savefig('../figs/uni_cdf.png')

#plt.savefig('../figs/gau_cdf.pdf')
#plt.savefig('../figs/gau_cdf.png')

#plt.savefig('../figs/log_cdf.pdf')
#plt.savefig('../figs/log_cdf.png')

#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
#plt.show() #opening the plot window

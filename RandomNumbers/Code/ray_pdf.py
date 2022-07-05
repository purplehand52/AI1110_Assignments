#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
import theo_func as t


maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
randvar = np.loadtxt('ray.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

vec_ray_pdf = np.vectorize(t.ray_pdf, otypes = [float])

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(x,vec_ray_pdf(x))#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$A_i$')
plt.ylabel('$p_A(A_i)$')
plt.legend(["Numerical","Theory"])
plt.savefig('../figs/ray_pdf.png')
plt.savefig('../figs/ray_pdf.pdf')
#else
#plt.show() #opening the plot window


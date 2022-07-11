#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import theo_func as t

#Points on X-Axis
x = np.linspace(0,10,20)

#Load Values (From Files)
randvar = np.loadtxt('peaRay_new.dat',dtype='double')

#Plot Y
plt.semilogy(x, randvar, 'o')

#Theoretical Function is just Q(A)
#q_vec = np.vectorize(t.q_func, otypes = [np.float])
#plt.plot(x, q_vec(x), 'g-')
#plt.semilogy(x, q_vec(x), 'r-')

#Create Grid and Labels
plt.grid()
plt.xlabel('A')
plt.ylabel('$P_{e}$')
#plt.show()

#Save Files
plt.savefig('../figs/pe_plotRay.pdf')
plt.savefig('../figs/pe_plotRay.png')

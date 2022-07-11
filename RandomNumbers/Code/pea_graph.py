#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import theo_func as t

#Points on X-Axis
x = np.linspace(0,10,20)

#Load Values (From Files)
randvar = np.loadtxt('pe_a.dat',dtype='double')

#Plot Y
plt.plot(x, randvar, 'o')

#Theoretical Function is just Q(A)
q_vec = np.vectorize(t.q_func, otypes = [np.float])
plt.plot(x, q_vec(x), 'g-')


#Create Grid and Labels
plt.grid()
plt.xlabel('A')
plt.ylabel('$P_{e}$')

#Semilog
plt.semilogy(x, q_vec(x), 'r-')

#plt.show()

#Save Files
plt.savefig('../figs/pea_plot_semi.pdf')
plt.savefig('../figs/pea_plot_semi.png')

#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import theo_func as t

#Points on X-Axis
x = np.linspace(0,1000,1000)

#Load Values (From Files)
randvar = np.loadtxt('y.dat',dtype='double')

#Plot Y
plt.plot(x, randvar[:1000], 'o')

#Create Grid and Labels
plt.grid()
plt.xlabel('Sample')
plt.ylabel('$Y$')

#Save Files
plt.savefig('../figs/y_plot.pdf')
plt.savefig('../figs/y_plot.png')

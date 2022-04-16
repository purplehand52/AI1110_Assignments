#Importing packages
import matplotlib.pyplot as plt
import numpy as np

#Define data values
#Plot 1
x1 = np.arange(-10, 10, 2, np.int8)
y1 = (x1 + 3)/2
plt.plot(x1, y1,'-')

#Plot 2
x2 = np.arange(-10, 10, 2, np.int8)
y2 = (4*x2 + 1)/5
plt.plot(x2, y2, '--')

#Label
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Regression Lines")
plt.grid()
plt.legend(["Line of y wrt x", "Line of x wrt y"])

#Save
plt.savefig("../figs/plot.png")
plt.show()

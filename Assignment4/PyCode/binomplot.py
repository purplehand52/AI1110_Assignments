from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

#SubPlot
fig1, (ax1, ax2) = plt.subplots(1, 2)

#Number of trials, probability of success
n = 2
p = 0.5

#Random Variables:Binomial
rv = binom(n, p)

#X_Values
x_val = np.arange((n+1))

#PROBABILITY_MASS_DISTRIBUTION
#Y_Values
pmf_val = rv.pmf(x_val)

#Plot
ax1.plot(x_val, pmf_val, 'bo')
ax1.vlines(x_val, 0, pmf_val, colors='k', label='Probability')
ax1.legend(loc = 'best', frameon = True)
ax1.set_title("Probability Mass Distribution") 

#CUMULATIVE_DISTRIBUTION
#Y_Values
cdf_val = rv.cdf(x_val)

#Plot
ax2.plot(x_val, cdf_val, 'bo')
ax2.vlines(x_val, 0, cdf_val, colors='k', label='Cumulative')
ax2.legend(loc = 'best', frameon = True)
ax2.set_title("Cumulative Distribution")

plt.savefig("../Figures/binom.png")

#Find probability where rv >= 1
#P(rv >= 1) = 1 - P(rv < 1) = 1 - P(rv = 0)
prob_rvzero = pmf_val[0]
ans = 1 - prob_rvzero
print("Required Probability =", ans)

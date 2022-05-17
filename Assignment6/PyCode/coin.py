from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

#Figure 1
plt.figure(1)

#Number of trials = 2, probability of success of getting heads
n_1 = 2
p_1 = 0.5

#Random Variables:Binomial
rv_1 = binom(n_1, p_1)

#X_Values
x_val_1 = np.arange((n_1+1))

#Y_Values
pmf_val_1 = rv_1.pmf(x_val_1)

#Plot
plt.plot(x_val_1, pmf_val_1, 'bo')
plt.vlines(x_val_1, 0, pmf_val_1, colors='k', label='Probability')
plt.legend(loc = 'best', frameon = True)

plt.savefig("../Figures/coin1.png")

#Figure 2
plt.figure(2)

#Number of trials = 3, probability of success of getting tails
n_2 = 3
p_2 = 0.5

#Random Variables:Binomial
rv_2 = binom(n_2, p_2)

#X_Values
x_val_2 = np.arange((n_2+1))

#Y_Values
pmf_val_2 = rv_2.pmf(x_val_2)

#Plot
plt.plot(x_val_2, pmf_val_2, 'bo')
plt.vlines(x_val_2, 0, pmf_val_2, colors='k', label='Probability')
plt.legend(loc = 'best', frameon = True)

plt.savefig("../Figures/coin2.png")

#Figure 1
plt.figure(3)

#Number of trials, probability of success of getting heads
n_3 = 4
p_3 = 0.5

#Random Variables:Binomial
rv_3 = binom(n_3, p_3)

#X_Values
x_val_3 = np.arange((n_3+1))

#Y_Values
pmf_val_3 = rv_3.pmf(x_val_3)

#Plot
plt.plot(x_val_3, pmf_val_3, 'bo')
plt.vlines(x_val_3, 0, pmf_val_3, colors='k', label='Probability')
plt.legend(loc = 'best', frameon = True)

plt.savefig("../Figures/coin3.png")

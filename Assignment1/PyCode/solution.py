#Import
import sympy as sp

#Import symbols
from sympy.abc import m, n

#Expression
exp = (7*m + 2*n)/(7*m - 2*n)

#Solves exp = 5/3 for m in terms of n
"""All solutions are given in a list, because we ony have a single solution we will get a singleton list """
ans = sp.solve(sp.Eq(exp, 5/3), m)

#Find m/n by simplifying to rational
exp1 = m/n
final_ratio = sp.nsimplify((ans[0]/n), rational = True)
print("Ratio", exp1, "=", final_ratio)

#Second Ratio by substituting m = ratio*n
exp2 = (m**2 + n**2)/(m**2 - n**2)
sndratio = exp2.subs(m, final_ratio * n)
print("Ratio", exp2, "=", sndratio)

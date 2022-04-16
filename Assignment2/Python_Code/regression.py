#Assignment 2
import sympy as sp
from sympy.abc import x, y

#Problem:
"""Find correlation coefficient from regression lines x - 2y + 3 = 0, 4x - 5y + 1 = 0"""

#Idea
"""If regression line of y on x : y = mx + c
and regression line of x on y: x = ny + c, then
correlation coefficent (r) = sqrt(mn)"""

""" m and n and r have the same sign"""

""" -1 < r < 1"""

#Writing line equations in SymPy (Note that there is only one solution of x in terms of y and vice versa)
line_1 = sp.Eq(x - 2*y + 3, 0)
line_2 = sp.Eq(4*x - 5*y + 1, 0)

#We shall assume that line_1 is regression line of y on x, line_2 is regression line of x on y
m = (sp.solve(line_1, y)[0]).coeff(x)
n = (sp.solve(line_2, x)[0]).coeff(y)

#Find r (and assign proper sign)
if ((m > 0) and (n > 0)):
	r = sp.sqrt(m * n)
else:
	r = -sp.sqrt(m * n)

#Check if r <= 1 and exchange lines otherwise and compute r similar to before
if(r <= 1):
    print("Correlation Coefficient: ", r)
else:
    m = (sp.solve(line_2, y)[0]).coeff(x)
    n = (sp.solve(line_1, x)[0]).coeff(y)
    if ((m > 0) and (n > 0)):
    	r = sp.sqrt(m*n)
    else:
    	r = -sp.sqrt(m*n)
    print("Correlation Coefficient: ", r)

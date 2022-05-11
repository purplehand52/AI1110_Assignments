#Import pandas
import pandas
import numpy

#Load data
numbers = pandas.read_excel("cond.xlsx")

#Sample Space
sample = numbers["Card Nos"].to_numpy()
n_s = len(sample)

#Random variable : X = 1
x = (sample%2 == 0)

#Random variable : Y = 1
y = (sample > 3)

#Random variable : Z = X^Y
z = (x & y)

#Prob(Y = 1)
prob_y = (numpy.count_nonzero(y))/n_s

#Prob(Z = X^Y)
prob_z = (numpy.count_nonzero(z))/n_s

#Prob(X|Y)
prob_xify = prob_z/prob_y
print("The required probability is", prob_xify)

#Import pandas
import pandas
import numpy

#Load data
weights = pandas.read_excel("flour.xlsx")

#Sample Space
sample = list(weights["Weights"])
n_s = len(sample)

#Favourable random variables : X > 5
n_x = numpy.count_nonzero(weights > 5)

#Answer
prob = n_x/n_s
print("The probability that random variable X > 5 is", prob);


import numpy as np

#Sample Space
PROB_RAND = 10000
SAMPLE_RAND = 10000

#Uniform RV for probability
prob = np.random.rand(PROB_RAND)
prob = (prob*0.2) + 0.4

#Values for finding number of heads out of sample space and assigning Boolean values
sample = np.random.rand(SAMPLE_RAND, PROB_RAND)
chk = sample < prob

ans = np.count_nonzero(chk)/(SAMPLE_RAND*PROB_RAND)
print("Probability is", ans)

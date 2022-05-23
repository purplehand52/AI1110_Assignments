import numpy as np

PROB_RAND = 10000
SAMPLE_RAND = 10000

prob = np.random.rand(PROB_RAND)
prob = (prob*0.2) + 0.4

sample = np.random.rand(SAMPLE_RAND, PROB_RAND)

chk = sample < prob

ans = np.count_nonzero(chk)/(SAMPLE_RAND*PROB_RAND)
print("Probability is", ans)

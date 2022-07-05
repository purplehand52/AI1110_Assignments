import math
import mpmath
import numpy as np

#Function1: Uniform Distribution CDF
def uni_cdf(x):
    if(x < 0):
        return(0)
    elif(x > 1):
        return(1)
    else:
        return(x)
        
#Function2: Gaussian CDF
#Q-Function
def q_func(x):
    return((1/2) * (1 - math.erf(x/math.sqrt(2))))

#Actual Function
def gau_cdf(x):
    return(1 - q_func(x))
    
#Function3: Gaussian PDF
def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)

#Function4: Log CDF
def log_cdf(x):
    if(x < 0):
        return(0)
    else:
        return(1 - math.exp(-x/2))

#Function5: Triangular CDF
def tri_cdf(x):
    if(x < 0):
        return(0)
    elif((x >= 0) and (x < 1)):
        return(x*x/2)
    elif((x >= 1) and (x < 2)):
        return(1 - (x-2)*(x-2)/2)
    else:
        return(1)
        
#Function6: Triangular PDF
def tri_pdf(x):
    if(x < 0):
        return(0)
    elif((x >= 0) and (x < 1)):
        return(x)
    elif((x >= 1) and (x < 2)):
        return(2-x)
    else:
        return(0)

#Function7: Returns Probability of Error
def prob_err():
    #Load Text
    b_val = np.loadtxt('ber.dat', dtype='double')
    y_val = np.loadtxt('y.dat', dtype='double')

    #Check for P(e|0)
    b_1 = np.count_nonzero(b_val > 0)
    y_neg = np.count_nonzero((y_val < 0) & (b_val > 0))
    p_e0 = y_neg/b_1

    #Check for P(e|1)
    b_0 = np.count_nonzero(b_val < 0)
    y_pos = np.count_nonzero((y_val > 0) & (b_val < 0))
    p_e1 = y_pos/b_0

    #Check for P(e)
    p_e = (p_e1 + p_e0)/2

    #Return array
    return([p_e0, p_e1, p_e])
    
#Function8: Chi PDF
def chi_pdf(x):
	if(x < 0):
		return(0)
	else:
		return(math.exp(-x/2)/2)
		
#Function9: Chi CDF
def chi_cdf(x):
	if(x < 0):
		return(0)
	else:
		return(1 - math.exp(-x/2))

#Function10: Ray CDF
def ray_cdf(x):
	if(x < 0):
		return(0)
	else:
		return(1 - math.exp(-x**2/2))

#Function11: Ray PDF
def ray_pdf(x):
	if(x < 0):
		return(0)
	else:
		return(x * math.exp(-x**2/2))

########################################################## README ###########################################################

# This file implements STDP curve and weight update rule

##############################################################################################################################



import numpy as np
from matplotlib import pyplot as plt
from parameters import param as par

#STDP reinforcement learning curve
def rl(t):
	
	if t>0:
		return -par.A_plus*np.exp(-float(t)/par.tau_plus)
	if t<=0:
		return par.A_minus*np.exp(float(t)/par.tau_minus)


#STDP weight update rule
def update(w, del_w):
	if del_w<0:
		return w + par.sigma*del_w*(w-abs(par.w_min))*par.scale
	elif del_w>0:
		return w + par.sigma*del_w*(par.w_max-w)*par.scale

if __name__ == '__main__':
	
	print rl(-20)*par.sigma

	
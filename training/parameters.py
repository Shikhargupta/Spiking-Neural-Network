################################################ README #########################################################

# This file contains all the parameters of the network.

#################################################################################################################

class param:
	scale = 1
	T = 200
	t_back = -20
	t_fore = 20

	pixel_x = 28
	Prest = 0
	m = pixel_x*pixel_x #Number of neurons in first layer
	n =  3  #Number of neurons in second layer
	Pmin = -500*scale
	# Pth = 5
	# D = 0.7
	w_max = 1.5*scale
	w_min = -1.2*scale
	sigma = 0.1 #0.02
	A_plus = 0.8  # time difference is positive i.e negative reinforcement
	A_minus = 0.3 # 0.01 # time difference is negative i.e positive reinforcement 
	tau_plus = 8
	tau_minus = 5
	
	epoch = 12


	fr_bits = 12
	int_bits = 12
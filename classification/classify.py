import numpy as np
from neuron import neuron
import random
from recep_field import rf
import cv2
from spike_train import encode
from weight_initialization import learned_weights_x
from weight_initialization import learned_weights_o

#Parameters
global time, T, dt, t_back, t_fore, w_min
T = 200
time  = np.arange(1, T+1, 1)
t_back = -20
t_fore = 20
Pth = 5.5
m = 256 #Number of neurons in first layer
n = 4 #Number of neurons in second layer

layer2 = []

# creating the hidden layer of neurons
for i in range(n):
	a = neuron()
	layer2.append(a)

#synapse matrix	
synapse = np.zeros((n,m))

#learned weights
synapse[0] = learned_weights_x()
synapse[1] = learned_weights_o()

#random initialization for rest of the synapses
for i in range(2,n):
	for j in range(m):
		synapse[i][j] = random.uniform(-0.2,0.2)

for k in range(1):

	for i in range(2):
		spike_count = [0,0,0,0]
    
		#read the image to be classified
		img = cv2.imread("images2/" + str(i) + ".png", 0)
		
    #initialize the potentials of output neurons
    for x in layer2:
			x.initial()
    
    #calculate teh membrane potentials of input neurons
		pot = rf(img)
    
    #generate spike trains
		train = np.array(encode(pot))
    
    #flag for lateral inhibition
		f_spike = 0
    
		active_pot = [0,0,0,0]

		for t in time:
			for j, x in enumerate(layer2):
				active = []
        
        #update potential if not in refractory period
				if(x.t_rest<t):
					x.P = x.P + np.dot(synapse[j], train[:,t])
					if(x.P>x.Prest):
						x.P -= x.D
					active_pot[j] = x.P
			
			# Lateral Inhibition		
			if(f_spike==0):
				high_pot = max(active_pot)
				if(high_pot>Pth):
					f_spike = 1
					winner = np.argmax(active_pot)
					for s in range(n):
						if(s!=winner):
							layer2[s].P -= Pth/2

			#Check for spikes				
			for j,x in enumerate(layer2):
				s = x.check()
				if(s==1):
					spike_count[j] += 1
					x.t_rest = t + x.t_ref
		print spike_count

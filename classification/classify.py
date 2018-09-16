##################### README ###################################################
# This file executes the classification algorithm over input testing images.
# Winner neurons inhibit other neurons by a phenomenon called Lateral inhibition
# Spike for each output neuron at each time stamp is monitored.
################################################################################
import numpy as np
from neuron import neuron
import random
from recep_field import rf
import imageio
from spike_train import *
from weight_initialization import learned_weights

#Parameters
global time, T, dt, t_back, t_fore, w_min
T = 200
time  = np.arange(1, T+1, 1)
t_back = -20
t_fore = 20
Pth = 150 #Should be Pth = 6 for deterministic spike train
m = 784 #Number of neurons in first layer
n = 8 #Number of neurons in second layer
epoch = 1
num_of_images = 6
w_max = 0.5
w_min = -0.5

layer2 = []
# creating the hidden layer of neurons
for i in range(n):
	a = neuron()
	layer2.append(a)

#synapse matrix
synapse = np.zeros((n,m))
#learned weights
weight_matrix = learned_weights()
for i in range (num_of_images):
	synapse[i] = weight_matrix[i]

#random initialization for rest of the synapses
for i in range(num_of_images,n):
	for j in range(m):
		synapse[i][j] = random.uniform(w_min,w_max)

for k in range(epoch):
	for i in range(1,7):
		spike_count = np.zeros((n,1))

		#read the image to be classified
		img = imageio.imread("training_images/" + str(i) + ".png")

    	#initialize the potentials of output neurons
		for x in layer2:
			x.initial()

    #calculate teh membrane potentials of input neurons
		pot = rf(img)

    #generate spike trains. Select between deterministic and stochastic
		# train = np.array(encode_deterministic(pot))
		train = np.array(encode_stochastic(img))

    #flag for lateral inhibition
		f_spike = 0
		active_pot = np.zeros((n,1))
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
							layer2[s].P = layer2[s].Pmin

			#Check for spikes
			for j,x in enumerate(layer2):
				s = x.check()
				if(s==1):
					spike_count[j] += 1
					x.t_rest = t + x.t_ref
		print spike_count

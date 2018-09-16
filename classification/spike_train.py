########################### README ############################################
# This file is used to generate spike train from potential map. There are two
# methods to do so. One is deterministic where we calculate the spike frequency
# directly proportional to the potential of that pixel and construct a train
# with equally spaced spikes. Other one is stochastic where we calculate the
# probability of the pixel to fire a spike and construct a spike train
# accordingly
###############################################################################

import numpy as np
from numpy import interp
from neuron import neuron
import random
from recep_field import rf
import imageio
import math
from sklearn.preprocessing import normalize

# Builds a probabilistic spike train
def encode_stochastic(img):
	T = 200
	train = []
	pot1 = normalize(img, norm='l2')
	for l in range(28):
		for m in range(28):
			temp = np.random.uniform(size=(T+1))
			temp = (temp < pot1[l][m])
			train.append(temp)
	return train

def encode_deterministic(pot):
	#defining time frame of 1s with steps of 5ms
	T = 200;
	#initializing spike train
	train = []

	for l in range(28):
		for m in range(28):
			temp = np.zeros([(T+1),])
			#calculating firing rate proportional to the membrane potential
			freq = interp(pot[l][m], [-2,5], [1,20])
			# print freq
			if freq>0:
				freq1 = math.ceil(T/freq)
				#generating spikes according to the firing rate
				k = freq1
				while k<(T+1):
					temp[int(k)] = 1
					k = k + freq1
			train.append(temp)
			# print sum(temp)
	return train


if __name__  == '__main__':
	m = []
	n = []
	img = imageio.imread("training_images/1.png")
	# pot = rf(img)
	# train = encode_deterministic(pot)
	# print train
	# print img
	encode_stochastic(img)

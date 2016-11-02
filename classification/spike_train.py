import numpy as np
from numpy import interp
from neuron import neuron
import random
from matplotlib import pyplot as plt
from recep_field import rf
import cv2
from rl import rl
from rl import update
import math
def encode(pot):

	#defining time frame of 1s with steps of 5ms
	T = 200;
	# dt = 0.005
	# time  = np.arange(0, T+dt, dt)

	#initializing spike train
	train = []

	for l in range(16):
		for m in range(16):
		
			temp = np.zeros([(T+1),])

			#calculating firing rate proportional to the membrane potential
			freq = interp(pot[l][m], [-2,5], [1,20])
			
			# print freq
			if freq>0:
				
				freq1 = math.ceil(T/freq)

				#generating spikes according to the firing rate
				k = freq1
				while k<(T+1):
					temp[k] = 1
					k = k + freq1
			train.append(temp)
			# print sum(temp)
	return train

if __name__  == '__main__':
	m = []
	n = []
	img = cv2.imread("images/" + str(511) + ".png", 0)
	pot = rf(img)
	for i in pot:
		m.append(max(i))
		n.append(min(i))

	print max(m), min(n)
	train = encode(pot)
	for x in train:
		print sum(x)



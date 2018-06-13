######################################################## README #############################################################

# This file generates rate based spike train from the potential map.

############################################################################################################################


import numpy as np
from numpy import interp
from snn.neuron import neuron
import random
from matplotlib import pyplot as plt
from snn.recep_field import rf
import imageio
from snn.rl import rl
from snn.rl import update
import math
from snn.parameters import param as par

def encode(pot):

	#initializing spike train
	train = []

	for l in range(par.pixel_x):
		for m in range(par.pixel_x):

			temp = np.zeros([(par.T+1),])


			#calculating firing rate proportional to the membrane potential
			freq = interp(pot[l][m], [-1.069,2.781], [1,20])
			#print(pot[l][m], freq)
			# print freq
			if freq<=0:
				print(error)

			freq1 = math.ceil(600/freq)

			#generating spikes according to the firing rate
			k = freq1
			if(pot[l][m]>0):
				while k<(par.T+1):
					temp[k] = 1
					k = k + freq1
			train.append(temp)
			# print sum(temp)
	return train

if __name__  == '__main__':
	# m = []
	# n = []
	img = imageio.imread("../images/100.png")

	pot = rf(img)

	# for i in pot:
	# 	m.append(max(i))
	# 	n.append(min(i))

	# print max(m), min(n)
	train = encode(pot)
	f = open('train6.txt', 'w')
	print(np.shape(train))

	for j in range(len(train)):
		for i in range(len(train[j])):
			f.write(str(int(train[j][i])))
		f.write('\n')

	f.close()
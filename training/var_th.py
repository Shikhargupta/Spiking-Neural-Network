############################################## README #################################################

# This calculates threshold for an image depending upon its spiking activity.

########################################################################################################


import numpy as np
from neuron import neuron
import random
from matplotlib import pyplot as plt
from recep_field import rf
import cv2
from spike_train import encode
from rl import rl
from rl import update
from reconstruct import reconst_weights
from parameters import param as par
import os


def threshold(train):

	tu = np.shape(train[0])[0]
	thresh = 0
	for i in range(tu):
		simul_active = sum(train[:,i])
		if simul_active>thresh:
			thresh = simul_active

	return (thresh/3)*par.scale


if __name__ == '__main__':	

	# img = cv2.imread("mnist1/" + str(1) + ".png", 0)
	img = np.array(Image.open("mnist1/" + str(1) + ".png", 0))
	print img
	# pot = rf(img)
	# train = np.array(encode(pot))
	# print threshold(train)
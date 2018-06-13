###################################################### README #####################################################

# This file is used to leverage the generative property of a Spiking Neural Network. reconst_weights function is used
# for that purpose. Looking at the reconstructed images helps to analyse training process.

####################################################################################################################


import numpy as np
from numpy import interp
import imageio
from snn.recep_field import rf
from snn.parameters import param as par


def reconst_weights(weights, num):
	weights = np.array(weights)
	weights = np.reshape(weights, (par.pixel_x,par.pixel_x))
	img = np.zeros((par.pixel_x,par.pixel_x))
	for i in range(par.pixel_x):
		for j in range(par.pixel_x):
			img[i][j] = int(interp(weights[i][j], [par.w_min,par.w_max], [0,255]))

	imageio.imwrite('neuron' + str(num) + '.png', img)
	return img

def reconst_rf(weights, num):
	weights = np.array(weights)
	weights = np.reshape(weights, (par.pixel_x,par.pixel_x))
	img = np.zeros((par.pixel_x,par.pixel_x))
	for i in range(par.pixel_x):
		for j in range(par.pixel_x):
			img[i][j] = int(interp(weights[i][j], [-2,3.625], [0,255]))

	imageio.imwrite('neuron' + str(num) + '.png', img)
	return img


if __name__ == '__main__':

	img = imageio.imread("images2/" + "69" + ".png")
	pot = rf(img)
	reconst_rf(pot, 12)
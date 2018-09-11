################################ README ########################################
# This file is used to initialize the network with trained weights.'image_names'
# consists of names of the images that are needed to be read.
################################################################################

import numpy as np
import imageio

def learned_weights():
	image_names = ["1", "2", "3", "4", "5", "6"]
	ans = []
	for image in image_names:
		temp = []
		img = imageio.imread("training_images/" + image + ".png")
		for i in img:
			for j in i:
				if(j==0):
					temp.append(-0.7)
				else:
					temp.append(1)
		ans.append(temp)
	return ans

if __name__ == '__main__':
	a = learned_weights()
	print a

import numpy as np
from neuron import neuron
import random
from matplotlib import pyplot as plt
import cv2

def learned_weights_x():
	ans = []
	img = cv2.imread("images2/100.png", 0)
	for i in img:
		for j in i:
			if(j==0):
				ans.append(-0.5)
			else:
				ans.append(1.5)

	return ans

def learned_weights_o():
	ans = []
	img = cv2.imread("images2/101.png", 0)
	for i in img:
		for j in i:
			if(j==0):
				ans.append(-0.5)
			else:
				ans.append(1.5)

	return ans					

if __name__ == '__main__':
	a = learned_weights_x()
	print a

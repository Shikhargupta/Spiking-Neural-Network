import numpy as np
from neuron import neuron
import random
from matplotlib import pyplot as plt

from scipy import misc

def learned_weights_x():
	ans = []
	img = misc.imread("images/100.png", mode='L')
	for i in img:
		for j in i:
			if(j==0):
				ans.append(-0.5)
			else:
				ans.append(1.5)

	return ans

def learned_weights_o():
	ans = []
	img = misc.imread("images/101.png", mode='L')
	for i in img:
		for j in i:
			if(j==0):
				ans.append(-0.5)
			else:
				ans.append(1.5)

	return ans					

if __name__ == '__main__':
	a = learned_weights_x()
	print(a)

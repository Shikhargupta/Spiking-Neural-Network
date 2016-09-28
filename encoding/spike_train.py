import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

# Sliding window implementation of receptive field
w = np.zeros([5,5])
pot = np.zeros([16,16])
ran = [-2,-1,0,1,2]
ox = 2
oy = 2
w[ox][oy] = 1

for i in range(5):
	for j in range(5):
		d = abs(ox-i) + abs(oy-j)
		w[i][j] = (-0.375)*d + 1

#reading dataset image (16x16)
img = cv2.imread('1.png', 0)

#calculating potential map of the image (256 input neuron potential)
for i in range(16):
	for j in range(16):
		summ = 0
		for m in ran:
			for n in ran:
				if (i+m)>=0 and (i+m)<=15 and (j+n)>=0 and (j+n)<=15:
					summ = summ + w[ox+m][oy+n]*img[i+m][j+n]
		pot[i][j] = summ
    
#defining time frame of 1s with steps of 5ms
T = 1;
dt = 0.005
time  = np.arange(0, T+dt, dt)

#initializing spike train
train = []

for l in range(16):
	for m in range(16):
	
		temp = np.zeros([201,])
		#calculating firing rate proportional to the membrane potential
		freq = math.ceil(0.102*pot[l][m] + 52.02)
		freq1 = math.ceil(200/freq)

		#generating spikes according to the firing rate
		k = 0
		while k<200:
			temp[k] = 1
			k = k + freq1
		train.append(temp)

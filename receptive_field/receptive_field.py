import numpy as np
import random

#Initializing a random input matrix. During implementation this would be a 16x16 image
inp = np.random.randint(0, 255, size=(16,16))

w = np.zeros([5,5]) #5x5 window initialized with zeros
pot = np.zeros([16,16]) #Initializing membrane potential matrix for 256 input neurons 
ran = [-2,-1,0,1,2] #Weight vectors for the window
ox = 2 #Origin x coordinate in the window matrix
oy = 2 #Origin y coordinate in the window matrix
w[ox][oy] = 1 #Manhattan distance zero

#Assigning weights to matrix elements according to mahanttan distance from the origin 
for i in range(5):
	for j in range(5):
		d = abs(ox-i) + abs(oy-j)
		w[i][j] = (-0.375)*d + 1

#Calculating membrane potential for each of the 256 input neurons		
for i in range(16):
	for j in range(16):
		summ = 0
		for m in ran:
			for n in ran:
				if (i+m)>=0 and (i+m)<=15 and (j+n)>=0 and (j+n)<=15:
					summ = summ + w[ox+m][oy+n]*inp[i+m][j+n]
		pot[i][j] = summ

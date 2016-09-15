import numpy as np
import random
from matplotlib import pyplot as plt

#constant global parameters which are same for the whole network
global Pref, Pmin, Pth, D, Pspike, time, T, dt
T = 500
dt = 0.125
Pref = 0
Pmin = -1
Pth = 5
D = 1
Pspike = 4
t_ref = 5
time  = np.arange(0, T+dt, dt)

#neuron class which can be instantiated in the main function as many times as required. It follows the integrate and fire model. 
#The out function takes in the matrices of spikes and weights and returns the output train of spikes.
class neuron:
	def __init__(self):
		self.t_rest = 0
		self.Pn = np.zeros(len(time))
		self.spike = np.zeros(len(time))
	def out(self,S, w):
		for i, t in enumerate(time):
			if i==0:
				a1 = S[:,i]
				self.Pn[i] = np.dot(w,a1) - D
				self.spike[i] = 0
			else:
				if t<=self.t_rest:
					self.Pn[i] = Pref
					self.spike[i] = 0
				elif t>self.t_rest:
					if self.Pn[i-1]>Pmin:
						a1 = S[:,i]
						self.Pn[i] = self.Pn[i-1] + np.dot(w,a1) - 0.25
						self.spike[i] = 0
					else:
						self.Pn[i] = 0
						self.spike[i] = 0	
				if self.Pn[i]>=Pth:
					self.Pn[i] += Pspike
					self.t_rest = t + t_ref
					self.spike[i] = 1

		return self.spike			


if __name__=='__main__':
	m = 5 #Number of neurons in first layer
	n = 3 #Number of neurons in second layer
#creating two layers of m and n neurons
	layer1 = []
	layer2 = []

	for i in range(m):
		a = neuron()
		layer1.append(a)
	for i in range(n):
		a = neuron()
		layer2.append(a)	

#initialising synapse array with random integers
	synapse = np.random.randint(0, 5, size=(n,m))
	S_in = []

#initialising the input spike trains
	for l in range(m):
		temp = []
		for k in range(len(time)):
			a = random.randrange(0,2)
			temp.append(a)
		S_in.append(temp)

#output of the first layer
	out_l1 = []
	w_in = np.eye(m)
	S_in = np.array(S_in)
	for l in range(m):
		temp = []
		temp = layer1[l].out(S_in,w_in[l])
		out_l1.append(temp)
	out_l1 = np.array(out_l1)	
	
#output of the second layer which was fed with the output of the first layer
	out_l2 = []
	for l in range(n):
		temp  = []
		temp = layer2[l].out(out_l1,synapse[l])
		out_l2.append(temp)

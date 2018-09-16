########################### README #############################################
# This is a neuron class which holds all the parameters and functions associated
# with a neuron of the network.
################################################################################

import numpy as np

global Pref, Pmin, Pth, D, Prest
Pref = 0
Prest = 0
Pmin = -1
Pth = 140 #Should be Pth = 6 for deterministic spike train
D = 0.5

class neuron:
	def __init__(self):
		self.Pth = Pth
		self.t_ref = 4
		self.t_rest = -1
		self.P = Prest
		self.D = D
		self.Pmin = Pmin
		self.Prest = Prest
	#Check if membrane potential has crossed the thresold value
	def check(self):
		if self.P>= Pth:
			self.P = Pref
			return 1
		elif self.P < Pmin:
			self.P  = Prest
			return 0
		else:
			return 0
	#Lateral Inhibition
	def inhibit(self):
		self.P  = Pmin
	def initial(self):
		self.t_rest = -1
		self.P = Prest

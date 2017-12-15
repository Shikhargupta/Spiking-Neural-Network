############################################################ README ##############################################################

# This is neuron class which defines the dynamics of a neuron. All the parameters are initialised and methods are included to check
# for spikes and apply lateral inhibition.

###################################################################################################################################

import numpy as np
import random
from matplotlib import pyplot as plt
from parameters import param as par

class neuron:
	def __init__(self):
		self.t_ref = 30
		self.t_rest = -1
		self.P = par.Prest
	def check(self):
		if self.P>= self.Pth:
			self.P = par.Prest
			return 1	
		elif self.P < par.Pmin:
			self.P  = par.Prest
			return 0
		else:
			return 0
	def inhibit(self):
		self.P  = par.Pmin
	def initial(self, th):
		self.Pth = th
		self.t_rest = -1
		self.P = par.Prest
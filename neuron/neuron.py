from numpy import *
import random
from matplotlib import pyplot as plt

#defining time scale
T = 50;
dt = 0.125;
time  = arange(0, T+dt, dt)

#generating random spike train to be fed to neuron
S = []
for k in range(len(time)):
	a = random.randrange(0,2)
	S.append(a)

#initialising membrane potential vector
Pn = zeros(len(time))

#definig other parameters
Pref = 0 #resting potential
Pmin = -1 #minimum potential
Pth = 25 #threshold
D = 0.25 #leakage factor
Pspike = 4 #spike potential

count = 0 #refractory counter
t_ref = 5 #refractory period
t_rest = 0 

#updating membrane potential according to simplified equations
for i, t in enumerate(time):
	if i==0:
		Pn[i] = S[i] - D
	else:
		if t<=t_rest:
			Pn[i] = Pref
		elif t>t_rest:
			if Pn[i-1]>Pmin:
				Pn[i] = Pn[i-1] + S[i] - D
			else:
				Pn[i] = 0	
		if Pn[i]>=Pth:
			Pn[i] += Pspike
			t_rest = t + t_ref		

	

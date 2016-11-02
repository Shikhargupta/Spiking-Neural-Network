import numpy as np
from matplotlib import pyplot as plt

global w_max, w_min, sigma
w_max = 1.5
w_min = -0.5
sigma = 0.0625


def rl(t):
	A_plus = 0.6
	A_minus = 0.3
	tau_plus = 8
	tau_minus = 5
	

	if t>0:
		return -A_plus*np.exp(-t/tau_plus)
	if t<=0:
		return A_minus*np.exp(t/tau_minus)

def update(w, del_w):
	a = w + sigma*del_w
	if a<w_min:
		return w_min
	elif a>w_max:
		return w_max
	else:
		return a

if __name__ == '__main__':
	
	t = np.arange(-20,20,0.02)
	p = []
	for i in t:
		p.append(rl(i))

	plt.plot(t, p)
	plt.show()

	
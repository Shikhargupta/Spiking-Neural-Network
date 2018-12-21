

####################################################### README ####################################################################

# This is the main file which calls all the functions and trains the network by updating weights


#####################################################################################################################################


import numpy as np
from neuron import neuron
import random
from matplotlib import pyplot as plt
from recep_field import rf
import imageio
from spike_train import encode
from rl import rl, update
from reconstruct import reconst_weights
from parameters import param as par
from var_th import threshold
import os
import time as timing 

start = timing.time()
print ("shikhar", start)
#potentials of output neurons
pot_arrays = []
for i in range(par.n):
    pot_arrays.append([])

#time series
time  = np.arange(1, par.T+1, 1)

layer2 = []

# creating the hidden layer of neurons
for i in range(par.n):
    a = neuron()
    layer2.append(a)

#synapse matrix    initialization
synapse = np.zeros((par.n,par.m))

for i in range(par.n):
    for j in range(par.m):
        synapse[i][j] = random.uniform(0,par.w_max*0.5)

spike_probe = []
for i in range(par.n):
    spike_probe.append([(0, 0)])

for k in range(par.epoch):
    for i in range(3):
        #print(i,"  ",k)
        img = imageio.imread("training/{}.png".format(i))

        #Convolving image with receptive field
        pot = rf(img)

        #Generating spike train
        train = np.array(encode(pot))
        if k == 0:
            print(train.shape)
        #calculating threshold value for the image
        var_threshold = threshold(train)

        # print var_threshold
        # synapse_act = np.zeros((par.n,par.m))
        # var_threshold = 9
        # print var_threshold
        #var_D = (var_threshold*3)*0.07

        var_D = par.D

        for x in layer2:
            x.initial(par.Pth)

        #flag for lateral inhibition
        f_spike = 0

        img_win = 100

        active_pot = []
        for index1 in range(par.n):
            active_pot.append(0)

        #Leaky integrate and fire neuron dynamics
        for t in time:
            for j, x in enumerate(layer2):
                active = []
                if(x.t_rest<t):
                    x.P = x.P + np.dot(synapse[j], train[:,t])
                    if(x.P>par.Prest):
                        x.P -= var_D
                    active_pot[j] = x.P

                pot_arrays[j].append(x.P)

            # Lateral Inhibition
            if(f_spike==0):
                high_pot = max(active_pot)
                if(high_pot>par.Pth):
                    f_spike = 1
                    winner = np.argmax(active_pot)
                    img_win = winner
                    print("winner is " + str(winner))
                    for s in range(par.n):
                        if(s!=winner):
                            layer2[s].P = -500

            #Check for spikes and update weights
            for j,x in enumerate(layer2):
                s = x.check()
                if(s==1):
                    spike_probe[j].append((len(pot_arrays[j]), 1))
                    x.t_rest = t + x.t_ref
                    x.P = par.Prest
                    for h in range(par.m):
                        for t1 in range(-2,par.t_back-1, -1):
                            if 0<=t+t1<par.T+1:
                                if train[h][t+t1] == 1:
                                    # print "weight change by" + str(update(synapse[j][h], rl(t1)))
                                    synapse[j][h] = update(synapse[j][h], rl(t1))




                        for t1 in range(2,par.t_fore+1, 1):
                            if 0<=t+t1<par.T+1:
                                if train[h][t+t1] == 1:
                                    # print "weight change by" + str(update(synapse[j][h], rl(t1)))
                                    synapse[j][h] = update(synapse[j][h], rl(t1))

        if(img_win!=100):
            for p in range(par.m):
                if sum(train[p])==0:
                    synapse[img_win][p] -= 0.06*par.scale
                    if(synapse[img_win][p]<par.w_min):
                        synapse[img_win][p] = par.w_min

print ("total time taken", (timing.time() - start))
# ttt = np.arange(0,len(pot_arrays[0]),1)
# Pth = []
# for i in range(len(ttt)):
#     Pth.append(layer2[0].Pth)

# #plotting
# plt.figure(0)
# for i in range(par.n):
#     plt.subplot(par.n, 1, i+1)
#     axes = plt.gca()
#     axes.set_ylim([-20,60])
#     plt.plot(ttt,Pth, 'r')
#     plt.plot(ttt,pot_arrays[i])

# plt.figure(1)

# for i in range(par.n):
#     plt.subplot(par.n, 1, i+1)
#     axes = plt.gca()
#     axes.set_ylim([0, 1])
#     vals = np.array(spike_probe[i])
#     plt.stem(vals[:,0],vals[:,1])
# plt.show()

# plt.figure(2)
# for i in range(par.n):
#     plt.subplot(par.n/2, par.n/2, i+1)
#     plt.gca().grid(False)
#     weights = np.array(synapse[i])
#     weights = np.reshape(weights, (par.pixel_x,par.pixel_x))
#     img = np.zeros((par.pixel_x,par.pixel_x))
#     for i in range(par.pixel_x):
#         for j in range(par.pixel_x):
#             img[i][j] = np.interp(weights[i][j], [par.w_min,par.w_max], [-1.0,1.0])
#     plt.imshow(img)
#     plt.colorbar()
# plt.show()


# with open('weights_training.txt', 'w') as weight_file:
#     for i in range(len(synapse)):
#         weights = []
#         for j in synapse[i]:
#             weights.append(str(j))
#         convert = '\t'.join(weights)
#         weight_file.write("%s\n" % convert)

# #Reconstructing weights to analyse training
# for i in range(par.n):
#     reconst_weights(synapse[i],i+1)
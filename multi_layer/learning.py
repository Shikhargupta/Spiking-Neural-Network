

####################################################### README ####################################################################

# This is the main file which calls all the functions and trains the network by updating weights


#####################################################################################################################################


import numpy as np
from neuron import neuron
import random
from matplotlib import pyplot as plt
from recep_field import rf
import cv2
from spike_train import encode
from rl import rl
from rl import update
from reconstruct import reconst_weights
from parameters import param as par
from var_th import threshold
import os
import pickle
import sys

#@profile
def learning(learning_or_classify):

    #1 = learning, 0 = classify
    #learning_or_classify = 0
    print learning_or_classify
    if(learning_or_classify == 0):
        print "Starting classify..."
    elif(learning_or_classify == 1):
        print "Starting learning..."
    else:
        print "Error in argument, quitting"
        quit()

    if(learning_or_classify == 0):
        par.epoch = 1

    #potentials of output neurons
    pot_arrays = []
    pot_arrays.append([]) #because 0th layer do not require neuron model
    for i in range(1,par.num_layers):
        pot_arrays_this = []
        for j in range(0,par.num_layer_neurons[i]):
            pot_arrays_this.append([])
        pot_arrays.append(pot_arrays_this)
    print "created potential arrays for each layer..."

    Pth_array = []
    Pth_array.append([]) #because 0th layer do not require neuron model
    for i in range(1,par.num_layers):
        Pth_array_this = []
        for j in range(0,par.num_layer_neurons[i]):
            Pth_array_this.append([])
        Pth_array.append(Pth_array_this)
    print "created potential threshold arrays for each layer..."


    train_all = []
    for i in range(0,par.num_layers):
        train_this = []
        for j in range(0,par.num_layer_neurons[i]):
            train_this.append([])
        train_all.append(train_this)
    print "created spike trains for each layer..."

    #synapse matrix initialization
    synapse = [] #synapse[i] is the matrix for weights from layer i to layer i+1, assuming index from 0
    for i in range(0,par.num_layers-1):
        synapse_this = np.zeros((par.num_layer_neurons[i+1],par.num_layer_neurons[i]))
        synapse.append(synapse_this)

    if(learning_or_classify == 1):
        for layer in range(0,par.num_layers-1):
            for i in range(par.num_layer_neurons[layer+1]):
	        for j in range(par.num_layer_neurons[layer]):
	            synapse[layer][i][j] = random.uniform(0,0.4*par.scale)
    else:
        for layer in range(0,par.num_layers-1):
            for i in range(par.num_layer_neurons[layer+1]):
	        #for j in range(par.num_layer_neurons[layer]):
                filename = "weights/layer_"+str(layer)+"_neuron_"+str(i)+".dat"
                with open(filename,"rb") as f:
	            synapse[layer][i] = pickle.load(f)


    print "created synapse matrices for each layer..."


    #this contains neurons of all layers except first
    layers = [] #layers[i] is the list of neurons from layer i, assuming index from 0
    layer_this = []
    layers.append(layer_this) #0th layer is empty as input layer do not require neuron model

    #time series 
    time  = np.arange(1, par.T+1, 1)

    # creating each layer of neurons
    for i in range(1,par.num_layers):
        layer_this = []
        for i in range(par.num_layer_neurons[i]):
            a = neuron()
            layer_this.append(a)
        layers.append(layer_this)
    print "created neuron for each layer..."


    for k in range(par.epoch):
        for i in range(1,7):
            print "Epoch: ",str(k),", Image: ", str(i)
            if(learning_or_classify == 1):
                img = cv2.imread("training_images/" + str(i) + ".png", 0)
            else:
                img = cv2.imread("training_images/" + str(i) + ".png", 0)
                 

            #Convolving image with receptive field
            pot = rf(img)
            #print pot

            #training layers i and i+1, assuming 0 indexing, thus n layers require n-1 pairs of training 
            for layer in range(0,par.num_layers-1):
                print "Layer: ", str(layer)

                #Generating spike train when the first layer
                #else take the spike train from last layer
                if(layer == 0):
                    train_all[layer] = np.array(encode(pot))
                    train = np.array(encode(pot))
                else:
                    train_all[layer] = np.asarray(train_this_layer)
                    train = np.array(np.asarray(train_this_layer))

                #print train[1]

                #calculating threshold value for the image
                var_threshold = threshold(train)
                #print "var_threshold is ", str(var_threshold)

                # print var_threshold
                # synapse_act = np.zeros((par.n,par.m))
                # var_threshold = 9
                # print var_threshold
                # var_D = (var_threshold*3)*0.07

                var_D = 0.15*par.scale

                for x in layers[layer+1]:
                    x.initial(var_threshold)

                #flag for lateral inhibition
                f_spike = 0

                img_win = 100

                active_pot = []
                train_this_layer = []
                for index1 in range(par.num_layer_neurons[layer+1]):
                    active_pot.append(0)
                    train_this_layer.append([])

                #print synapse[layer].shape, train.shape
                #Leaky integrate and fire neuron dynamics
                for t in time:
                    #print "Time: ", str(t)
                    for j, x in enumerate(layers[layer+1]):
                        active = []	
                        if(x.t_rest<t):
                            x.P = x.P + np.dot(synapse[layer][j], train[:,t])
                            if(x.P>par.Prest):
                                x.P -= var_D
                            active_pot[j] = x.P

                        #pot_arrays[layer+1][j].append(x.P)
                        #Pth_array[layer+1][j].append(x.Pth)

                    # Lateral Inhibition
                    # Occurs in the training of second last and last layer
                    #if(f_spike==0 and layer == par.num_layers - 2 and learning_or_classify == 1):
                    if(f_spike==0 ):
                        high_pot = max(active_pot)
                        if(high_pot>var_threshold):
                            f_spike = 1
                            winner = np.argmax(active_pot)
                            img_win = winner
                            #print "winner is " + str(winner)
                            for s in range(par.num_layer_neurons[layer+1]):
                                if(s!=winner):
                                    layers[layer+1][s].P = par.Pmin

                    #Check for spikes and update weights				
                    for j,x in enumerate(layers[layer+1]):
                        pot_arrays[layer+1][j].append(x.P)
                        Pth_array[layer+1][j].append(x.Pth)
                        s = x.check()
                        train_this_layer[j].append(s)
                        if(learning_or_classify == 1):
                            if(s==1):
                                x.t_rest = t + x.t_ref
                                x.P = par.Prest
                                for h in range(par.num_layer_neurons[layer]):

                                    for t1 in range(-2,par.t_back-1, -1):
                                        if 0<=t+t1<par.T+1:
                                            if train[h][t+t1] == 1:
                                                # print "weight change by" + str(update(synapse[j][h], rl(t1)))
                                                synapse[layer][j][h] = update(synapse[layer][j][h], rl(t1))


                                    for t1 in range(2,par.t_fore+1, 1):
                                        if 0<=t+t1<par.T+1:
                                            if train[h][t+t1] == 1:
                                                # print "weight change by" + str(update(synapse[j][h], rl(t1)))
                                                synapse[layer][j][h] = update(synapse[layer][j][h], rl(t1))

                    for j in range(par.num_layer_neurons[layer+1]):
                        train_this_layer[j].append(0)


                #if(img_win!=100 and layer == par.num_layers - 2 ):
                if(img_win!=100 ):
                    for p in range(par.num_layer_neurons[layer]):
                        if sum(train[p])==0:
                            synapse[layer][img_win][p] -= 0.06*par.scale
                            if(synapse[layer][img_win][p]<par.w_min):
                                synapse[layer][img_win][p] = par.w_min

                #print train_this_layer
                #print synapse[0][0]

            
            train_all[par.num_layers-1] = np.asarray(train_this_layer)

            results_each_layer = 1
            if(results_each_layer):
                for layer in range(par.num_layers-1,par.num_layers):
                    for i in range(par.num_layer_neurons[layer]):
                        print "Layer"+ str(layer) + ", Neuron"+str(i+1)+": "+str(sum(train_all[layer][i]))

    
    #print classification results
#    if(learning_or_classify == 0):
        
    


    plot = 0
    if (plot == 1):
        for layer in range(par.num_layers-1,par.num_layers):
            ttt = np.arange(0,len(pot_arrays[layer][0]),1)
    
            #plotting 
            for i in range(par.num_layer_neurons[layer]):
                axes = plt.gca()
                axes.set_ylim([-20,50])
                plt.plot(ttt,Pth_array[layer][i], 'r' )
                plt.plot(ttt,pot_arrays[layer][i])
                plt.show()

    #Reconstructing weights to analyse training
    reconst = 1
    if(learning_or_classify != 1):
        reconst = 0

    if(reconst == 1):
        for layer in range(par.num_layers-1):
            siz_x = int(par.num_layer_neurons[layer]**(.5))
            siz_y = siz_x
            for i in range(par.num_layer_neurons[layer+1]):
                reconst_weights(synapse[layer][i],i+1,layer,siz_x,siz_y)

    #Dumping trained weights of last layer to file
    dump = 1
    if(learning_or_classify != 1):
        dump = 0
    if(dump == 1):
        for layer in range(par.num_layers-1):
            for i in range(par.num_layer_neurons[layer+1]):
                filename = "weights/"+"layer_"+str(layer)+"_neuron_"+str(i)+".dat"
                with open(filename,'wb') as f:
                    #f.write(str(synapse[layer][i]))
                    pickle.dump(synapse[layer][i],f)
    

if __name__ == '__main__':
    learning_or_classify = int(sys.argv[1])
    learning(learning_or_classify)

import numpy as np
from classification.neuron import neuron
import random
from matplotlib import pyplot as plt

from scipy import misc

def learned_weights_x():
    ans = []
    #img = misc.imread("images/100.png", mode='L')
    #for i in img:
    #    for j in i:
    #        if(j==0):
    #            ans.append(-0.5)
    #        else:
    #            ans.append(1.5)
    #
    with open('weights.txt', 'r') as weight_file:
        lines = weight_file.readlines()
        for i in lines[0].split('\t'):
            ans.append(float(i))
    return ans

def learned_weights_o():
    ans = []

    with open('weights.txt', 'r') as weight_file:
        lines = weight_file.readlines()
        for i in lines[1].split('\t'):
            ans.append(float(i))
    return ans

if __name__ == '__main__':
    a = learned_weights_x()
    print(a)

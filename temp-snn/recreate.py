#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math
import snn
import imageio
from snn.parameters import param as par
from snn.recep_field import rf
from snn.spike_train import encode, encode2

img = imageio.imread("/Users/johnsoni/Downloads/mnist_png/training/5/0.png")
#img = imageio.imread("data/training/0.png")

pot = rf(img)

# for i in pot:
#     m.append(max(i))
#     n.append(min(i))

# print max(m), min(n)
#train = encode2(img)
train = encode(pot)
f = open('train6.txt', 'w')
print(np.shape(train))

for j in range(len(train)):
    for i in range(len(train[j])):
        f.write(str(int(train[j][i])))
    f.write('\n')

f.close()

with open('train6.txt','r') as f:
    pixels = []
    for line in f:
        sum = 0
        for i in line:
            if i == '1':
                sum += 1
        pixels.append(sum)
    pixels = np.array(pixels, dtype='float64')
    pixels = pixels/np.max(pixels) * 255.0
    dim = int(math.sqrt(len(pixels)))
    img = np.array(pixels, dtype='uint8').reshape((dim, dim))
    plt.imshow(img)
    plt.show()

        
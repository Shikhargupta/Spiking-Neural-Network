# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15) 
# [GCC 7.3.0]
# Embedded file name: /home/vonfaust/data/snn/codebase/python_imple/training/reconstruct.py
# Compiled at: 2018-12-30 05:37:08
import numpy as np
from numpy import interp
import cv2
from recep_field import rf
from parameters import param as par

def reconst_weights(weights, num, layer, reshape_x, reshape_y):
    weights = np.array(weights)
    weights = np.reshape(weights, (reshape_x, reshape_y))
    img = np.zeros((reshape_x, reshape_y))
    for i in range(reshape_x):
        for j in range(reshape_y):
            img[i][j] = int(interp(weights[i][j], [par.w_min, par.w_max], [0, 255]))

    img = np.resize(img, (28, 28))
    cv2.imwrite('weights/layer_' + str(layer) + '_neuron_' + str(num) + '.png', img)
    return img


def reconst_rf(weights, num):
    weights = np.array(weights)
    weights = np.reshape(weights, (par.pixel_x, par.pixel_x))
    img = np.zeros((par.pixel_x, par.pixel_x))
    for i in range(par.pixel_x):
        for j in range(par.pixel_x):
            img[i][j] = int(interp(weights[i][j], [-2, 3.625], [0, 255]))

    cv2.imwrite('neuron' + str(num) + '.png', img)
    return img


if __name__ == '__main__':
    img = cv2.imread('images2/69.png', 0)
    pot = rf(img)
    reconst_rf(pot, 12)
# okay decompiling reconstruct.pyc

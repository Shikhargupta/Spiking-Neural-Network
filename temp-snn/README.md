# Spiking-Neural-Network

This project implements a very basic SNN library that supports a very simple image classification example.

While simple, the code here implements a variety of useful and important SNN functions and produces a functional classifier.

To read more look at [the docs](docs/README.md).

## Running
* cd into the root where the project is cloned
* run classification/classify.py

it will use pregenerated weights and output the results of classifying the test images

You can also run training/learning.py to generate a new weights file and output `neuron[1-3].png`
which will show the reconstructed weights. One neuron should look random, the other two will produce
a pattern similar to the O, and another a pattern similar to the X.

To use the new weights, the weights for the X must be on the first line of weights.txt and
the weights for the O on the second line. When the weights are generated the first line of weights_training.txt
will corrispond to the weights shown in neuron1.png, the second line to neuron2.png and so
on, reorder them if needed.
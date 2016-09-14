## Synapse

In neurobiology synapse is a junction between two nerve cells, consisting of a minute gap across which impulses pass by diffusion of a neurotransmitter. 
In an SNN, synapse is the weighted path for generated spikes from one neuron to the other connected neurons.
<p align="center">
  <img src="/images/1.jpg" width="500"/>
</p>

This is the implementation of a simple network of 2 layers with 5 neurons in the first layer and 3 in the second as shown in the figure. Each neuron in the first layer is connected to all the neurons in the second layer via synapse. Synapses are realised by a 2D matrix of size (5x3) initialised with random weights. 

This provides a framework for the SNN with learned weights so that it can be used for classification (or prediction). It can be expanded to any number of layers with any number of neurons in it.

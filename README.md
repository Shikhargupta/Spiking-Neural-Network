# Spiking-Neural-Network
This is the python implementation of hardware efficient spiking neural network. It includes the modified learning and prediction rules which could be realised on hardware and are enegry efficient. Aim is to develop a network which could be used for on-chip learning as well as prediction.

Spike-Time Dependent Plasticity (STDP) algorithm will be used to train the network.

<p align="center">
  <img src="http://www.kdnuggets.com/wp-content/uploads/neuron1.jpg" width="500"/>
</p>

## Network Elements
  * [Neuron](neuron/)
  * [Synapse](synapse/)
  * [Receptive field](receptive_field/)
  * [Spike train](encoding/)


## [SNN Simulator for Classification](classification/)
Assuming that we have learned the optimal weights of the network using the STDP algorithm (will be implemented next), this uses the weights to classify the input patterns into different classes. The simulator uses the 'winner-takes-all' strategy to supress the non firing neurons and produce distinguishable results. Steps involved while classifying the patterns are:

- For each input neuron membrane potential is calculated in its [receptive field](receptive_field/) (5x5 window).
- [Spike train](encoding/) is generated for each input neuron with spike frequency proportional to the membrane potential.
- Foe each image, at each time step, potential of the neuron is updated according to the input spike and the weights associated.
- First firing output neuron performs lateral inhibition on the rest of the output neurons. 
- Simulator checks for output spike.

### Results
The simulator was tested upon binary classification. It can be extended upto any number of classes. The images for two classes are:

<img src="images/100.png" width="50"/>          <img src="images/101.png" width="50"/>

Each of the classes were presented to the network for 1000 time units each. The activity of the neurons was recorded. Here are the graphs of the potential of output neurons versus time unit.

First 1000 TU corresponds to class1, next 1000 to class2. Red line indicates the threshold potential.

<img src="images/figure_11.png" width="300"/> <img src="images/figure_12.png" width="300"/> <img src="images/figure_13.png" width="300"/> <img src="images/figure_14.png" width="300"/>

The 1st output neuron is active for class1, 2nd is active for class2, and 3rd and 4th are mute for both the classes. Hence, by recording the total spikes in output neurons, we can determine the class to which the pattern belongs.


## [Training an SNN](training)
In the previous section we assumed that our network is trained i.e weights are learned using STDP and can be used to classify patterns. Here we'll see how STDP works and what all need to be taken care of while implementing this training algorithm.

### Spike Time Dependent Plasticity
STDP is actually a biological process used by brain to modify it's neural connections (synapses). Since the unmatched learning efficiency of brain has been appreciated since decades, this rule was incorporated in ANNs to train a neural network. Moulding of weights is based on the following two rules -
- Any synapse that contribute to the firing of a post-synaptic neuron should be made strong i.e it's value should be increased.
- Synapses that don't contribute to the firing of a post-synaptic neuron should be dimished i.e it's value should be decreased.

Here is an explanation of how this algorithm works:

Consider the scenario depicted in this figure

<p align="center">
  <img src="images/spikes.jpg" width="350"/>
</p>

Four neurons connect to a single neuron by synapse. Each pre synaptic neuron is firing at its own rate and the spikes are sent forward by the corresponding synapse. The intensity of spike translated to post synaptic neuron depends upon the strength of the connecting synapse. Now, because of the input spikes membrane potential of post synaptic neuron increases and sends out a spike after crossing the threshold. At the time when post synaptic neuron spikes, we'll monitor which all pre synaptic neurons helped it to fire. This could be done by observing which pre synaptic neurons sent out spikes before post synaptic neuron spiked. This way they helped in post synaptic spike by increasing the membrane potential and hence the corresponding synapse is strengthend. The factor by which the weight of synapse is increased is inversly proportional to the time difference between post synaptic and pre synaptic spikes given by this graph

<p align="center">
  <img src="images/stdp_curve.jpg" width="400"/>
</p>

## Generative Property of SNN

## Variable Threshold

## Lateral Inhibition

## Training for 5 class dataset

## Parameters

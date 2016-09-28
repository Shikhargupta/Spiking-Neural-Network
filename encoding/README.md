# Generating Spike Trains

Input neuron layer has to be fed with the stimulus caused by its receptive field. Stimulus calculated from sliding window is an analog value and has to be converted into a spike train so that neuron can understand it. This encoder serves as an interface between numerical data (from the physical world, digital simulations, etc) and SNNs. It makes the conversion of information to artificial neuron spikes. The type of encoding adopted here is **rate coding**. It suggests that the information is carried by the firing rate of the neuron. Hence, spike train generated has frequency proportional to the corresponding membrane potential.

The average firing rate of retinal ganglion neurons lies between 1-200 Hz therefore the potential is scaled accordingly. Here are some examples of varying firing rates
<p align="center">
  <img src="/images/train.png" width="500"/>
</p>
<p align="center">
  <img src="/images/2.png" width="500"/>
</p>
<p align="center">
  <img src="/images/3.png" width="500"/>
</p>

The image used as the input is the one from the [semeion dataset] (https://archive.ics.uci.edu/ml/machine-learning-databases/semeion/) of handwritten integers
<p align="center">
  <img src="/images/test.png" width="100"/>
</p>

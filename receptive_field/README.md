# Receptive Field

Receptive field is an area in which stimulation leads to response of a particular sensory neuron. In the case of an SNN, where the input is an image, receptive field of a sensory neuron is the part of the image which increases the its membrane potential. Here on-centered receptive field is used. 
<p align="center">
  <img src="/images/center.png" width="200"/>
</p>
To realise an on centerd receptive field, a sliding window is used whose cells are weighted according to the [Manhattan Distance] (https://xlinux.nist.gov/dads/HTML/manhattanDistance.html) from the centre of the window. The fields for different neurons are overlapping.
<p align="center">
  <img src="/images/rf.png" width="200"/>
</p>

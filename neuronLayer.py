import neuron

class NeuronLayer(object):
    def __init__(self,numOfNeurons,inputsPerNeuron):
        self.neurons = [neuron.Neuron(inputsPerNeuron) for i in xrange(numOfNeurons)]

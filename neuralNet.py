from neuronLayer import NeuronLayer

class NeuralNet(object):
    def __init__(self,numOfInputs,numOfOutputs,
            numOfHiddenLayers,neuronsPerHiddenLayer):
        self.numOfInputs = numOfInputs
        self.numOfOutputs = numOfOutputs
        self.numOfHiddenLayers = numOfHiddenLayers
        self.neuronsPerHiddenLayer = neuronsPerHiddenLayer
        self.layers = [NeuronLayer(neuronsPerHiddenLayer,numOfInputs)]
        for i in xrange(1,numOfHiddenLayers):
            self.layers.append(NeuronLayer(neuronsPerHiddenLayer,neuronsPerHiddenLayer))
        self.layers.append(NeuronLayer(numOfOutputs,neuronsPerHiddenLayer))

    def putWeights(self,genes):
        index = 0
        for layer in self.layers:
            for neuron in layer.neurons:
                neuron.weights = genes[index:index+neuron.numOfInputs+1]
                index += neuron.numOfInputs + 1

    def getOutput(self):
        pass



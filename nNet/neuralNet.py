from neuronLayer import NeuronLayer
import math

def sigmoid(x):
    return 1.0/(1.0+math.exp(-x))

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

    def getOutput(self,inputs):
        out = []
        inp = inputs[:]
        for layer in self.layers:
            out = []
            for neuron in layer.neurons:
                val = 0
                for i in xrange(len(neuron.weights)-1):
                    val += inp[i] * neuron.weights[i]
                val -= neuron.weights[-1]
                out.append(sigmoid(val))
            inp = out[:]
        return out

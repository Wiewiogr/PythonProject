import unittest
import neuralNet

class TestNeuralNet(unittest.TestCase):
    def test_NeuralNetCreate(self):
        nn = neuralNet.NeuralNet(4,4,1,6)

    def test_numberOfLayers(self):
        nn = neuralNet.NeuralNet(4,4,1,6)
        self.assertEqual(len(nn.layers),2)
        nn = neuralNet.NeuralNet(4,4,3,6)
        self.assertEqual(len(nn.layers),4)

    def test_numberOfNeurons(self):
        nn = neuralNet.NeuralNet(4,4,1,6)
        self.assertEqual(len(nn.layers[0].neurons),6)
        self.assertEqual(len(nn.layers[1].neurons),4)

    def test_putWeights(self):
        nn = neuralNet.NeuralNet(4,4,1,6)
        numberOfWeights = (4+1)*6+(6+1)*4
        weights = [1 for i in range(numberOfWeights)]
        nn.putWeights(weights)
        for neuron in nn.layers[0].neurons:
            self.assertEqual(len(neuron.weights),5)
        for neuron in nn.layers[1].neurons:
            self.assertEqual(len(neuron.weights),7)

    def test_getOutput(self):
        nn = neuralNet.NeuralNet(4,4,1,6)
        numberOfWeights = (4+1)*6+(6+1)*4
        weights = [1 for i in range(numberOfWeights)]
        nn.putWeights(weights)
        in_ = [1,1,1,1]
        self.assertEqual(len(nn.getOutput(in_)),4)


if __name__ == '__main__':
    unittest.main(verbosity=2)

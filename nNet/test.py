import unittest
import controller

class TestController(unittest.TestCase):
    def test_ControllerCreate(self):
        contr = controller.Controller(40,4,4,1,6,0.7,0.05)
        self.assertEqual(True,True)

    def test_evolution(self):
        contr = controller.Controller(40,4,4,1,6,0.7,0.05)
        fit = [i for i in range(40)]
        contr.updateFitness(fit)
        contr.evolve()

    def test_numberOfNeuronWeightsInLayers(self):
        contr = controller.Controller(40,4,4,1,6,0.7,0.05)

        for neuron in contr.neuralNets[0].layers[0].neurons:
            self.assertEqual(len(neuron.weights),5)

        for neuron in contr.neuralNets[0].layers[1].neurons:
            print neuron.weights
            self.assertEqual(len(neuron.weights),7)


if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest
import controller

class TestTreeMethods(unittest.TestCase):
    def test_ControllerCreate(self):
        contr = controller.Controller(40,4,4,1,6,0.7,0.05)
        self.assertEqual(True,True)

if __name__ == '__main__':
    unittest.main(verbosity=2)

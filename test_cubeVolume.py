import unittest
from cubeVolume import cubeVolume

class TestCubeVolume(unittest.TestCase):

    def test_cubeVolume(self):
        self.assertEqual(cubeVolume(3), 27)

    def test_negativeCubeVolume(self):
        self.assertEqual(cubeVolume(-1), -1)

    def test_nonIntegerCubeVolume(self):
        self.assertEqual(cubeVolume("string"), -1)

if __name__ == "__main__":
    unittest.main()
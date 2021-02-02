import unittest
from averageElements import averageElements

class TestAverageElements(unittest.TestCase):

    def test_averageElements(self):
        self.assertEqual(averageElements([1, 2, 3, 4, 5]), 3)

    def test_emptyAverageElements(self):
        self.assertEqual(averageElements([]), None)

    def test_nonListAverageElements(self):
        self.assertEqual(averageElements("string"), None)

if __name__ == "__main__":
    unittest.main()


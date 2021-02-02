import unittest
import increment_decrement

class TestIncrementDecrement(unittest.TestCase):

    def test_increment(self):
        self.assertEqual(increment_decrement.increment(10), 13)

    def test_decrement(self):
        self.assertEqual(increment_decrement.decrement(10), 9)

if __name__ == "__main__":
    unittest.main(verbosity=2)
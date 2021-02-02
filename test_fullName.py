import unittest
from fullName import fullName

class TestFullName(unittest.TestCase):

    def test_fullName(self):
        self.assertEqual(fullName("Paul", "Lim"), "Paul Lim")

    def test_nonAlphanumericFullName(self):
        self.assertEqual(fullName("Paul", 2), None)

    def test_emptyFullName(self):
        self.assertEqual(fullName("Paul", ""), None)

if __name__ == "__main__":
    unittest.main()
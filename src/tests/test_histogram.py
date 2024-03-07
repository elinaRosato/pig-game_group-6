import unittest
from unittest.mock import patch
from game import Histogram

class TestHistogram(unittest.TestCase):

    # Set up
    def setUp(self):
        self.histogram = Histogram()
    
    def test_initialization(self):
        """
        Test the initialization of the Histogram class.
        """
        expected_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        self.assertEqual(self.histogram.counts, expected_counts)

if __name__ == '__main__':
    unittest.main()
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
    
    # Add roll with valid and invalid roll
    def test_add_roll_valid(self):
        """
        Test adding a valid roll to the histogram.
        """
        self.histogram.add_roll(3)
        expected_counts = {1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 0}
        self.assertEqual(self.histogram.counts, expected_counts)
    
    def test_add_roll_invalid_type(self):
        """
        Test adding a roll with an invalid type and expect a TypeError.
        """
        # Test case 1: Invalid roll (string)
        with self.assertRaises(TypeError):
            self.histogram.add_roll("invalid")

        # Test case 2: Invalid roll (float)
        with self.assertRaises(TypeError):
            self.histogram.add_roll(1.23)

        # Test case 3: Invalid roll (bool)
        with self.assertRaises(TypeError):
            self.histogram.add_roll(False)
    
    def test_add_roll_invalid_value(self):
        """
        Test adding a roll with an invalid value and expect a ValueError.
        """
        with self.assertRaises(ValueError):
            self.histogram.add_roll(7)

if __name__ == '__main__':
    unittest.main()
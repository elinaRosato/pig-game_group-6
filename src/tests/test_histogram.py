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
        
        # Test case 3: Invalid roll (None)
        with self.assertRaises(TypeError):
            self.histogram.add_roll(None)
    
    def test_add_roll_invalid_value(self):
        """
        Test adding a roll with an invalid value and expect a ValueError.
        """
        # Test case 1: Roll value below the valid range
        with self.assertRaises(ValueError):
            self.histogram.add_roll(0)

        # Test case 1: Roll value below the valid range
        with self.assertRaises(ValueError):
            self.histogram.add_roll(7)
    
    # Display
    @patch('builtins.print')
    def test_display(self, mock_print):
        """
        Test displaying the histogram.
        """
        self.histogram.add_roll(2)
        self.histogram.add_roll(4)
        expected_output = "Dice Roll Histogram:\n1: \n2: *\n3: \n4: *\n5: \n6: "
        self.histogram.display()
        mock_print.assert_called_with(expected_output)

if __name__ == '__main__':
    unittest.main()
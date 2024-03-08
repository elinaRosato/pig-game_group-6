import sys
import io
import unittest
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
    
    def test_display_output(self):
        """Test if display method prints the histogram correctly."""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.histogram.add_roll(1)
        self.histogram.add_roll(2)
        self.histogram.display()
        sys.stdout = sys.__stdout__
        expected_output = "Dice Roll Histogram:\n1: *\n2: *\n3: \n4: \n5: \n6: \n"
        self.assertEqual(captured_output.getvalue(), expected_output)
  
if __name__ == '__main__':
    unittest.main()
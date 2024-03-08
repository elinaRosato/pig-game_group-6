import unittest
import dicehand

class TestDiceHand(unittest.TestCase):

    def setUp(self):
        self.dice_hand = dicehand.DiceHand()

    def test_roll_dice_invalid_input_zero(self):
        """Test if rolling the dice with zero as an integer input raises ValueError."""
        with self.assertRaises(ValueError):
            self.dice_hand.roll_dice(0)

    def test_roll_dice_invalid_input_negative_integer(self):
        """Test if rolling the dice with a negative integer as an input raises ValueError."""
        with self.assertRaises(ValueError):
            self.dice_hand.roll_dice(-1)

    def test_roll_dice_positive_integer(self):
        """Test if rolling the dice with a positive integer as an input returns a list of results."""
        num_rolls = 5
        rolls = self.dice_hand.roll_dice(num_rolls)
        self.assertEqual(len(rolls), num_rolls)
        for roll in rolls:
            self.assertIsInstance(roll, int)
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)

    def test_roll_dice_invalid_input_negative_float(self):
        """Test if rolling the dice with negative float as an input raises ValueError.
           First it's checked if the number is negative and later its type is checked."""
        with self.assertRaises(ValueError):
            self.dice_hand.roll_dice(-1.5)

    def test_roll_dice_invalid_input_positive_float(self):
        """Test if rolling the dice with positive float as an input raises TypeError."""
        with self.assertRaises(TypeError):
            self.dice_hand.roll_dice(1.5)

    def test_roll_dice_invalid_input_letter(self):
        """Test if rolling the dice with letter as an input raises TypeError."""
        with self.assertRaises(TypeError):
            self.dice_hand.roll_dice('d')

    def test_roll_dice_invalid_input_None(self):
        """Test if rolling the dice with None as an input raises TypeError."""
        with self.assertRaises(TypeError):
            self.dice_hand.roll_dice(None)

    def test_roll_dice_invalid_input_true_boolean(self):
        """Test if rolling the dice with boolean True as an input raises TypeError."""
        with self.assertRaises(TypeError):
            self.dice_hand.roll_dice(True)

    def test_roll_dice_invalid_input_false_boolean(self):
        """Test if rolling the dice with boolean False as an input raises TypeError."""
        with self.assertRaises(TypeError):
            self.dice_hand.roll_dice(False)

    def test_roll_dice_count_matches_result_count(self):
        """Test that when rolling the dice a specified number of times (num_rolls), the length
           of the resulting list of integer values (rolls) matches with the number of rolls."""
        num_rolls = 100
        rolls = self.dice_hand.roll_dice(num_rolls)
        self.assertEqual(len(rolls), num_rolls)

if __name__ == '__main__':
    unittest.main()
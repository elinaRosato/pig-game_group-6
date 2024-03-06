import unittest
import dicehand

class TestDiceHand(unittest.TestCase):

    def setUp(self):
        self.dice_hand = dicehand.DiceHand()
        
    def test_roll_dice_invalid_input_zero(self):
        with self.assertRaises(ValueError):
            self.dice_hand.roll_dice(0)
            
    def test_roll_dice_invalid_input_negative_integer(self):
        with self.assertRaises(ValueError):
            self.dice_hand.roll_dice(-1)
            
    def test_roll_dice_positive_integer(self):
        num_rolls = 5
        rolls = self.dice_hand.roll_dice(num_rolls)
        self.assertEqual(len(rolls), num_rolls)
        for roll in rolls:
            self.assertIsInstance(roll, int)
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)
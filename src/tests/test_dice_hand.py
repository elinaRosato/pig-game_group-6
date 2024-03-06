import unittest
import dicehand

class TestDiceHand(unittest.TestCase):

    def setUp(self):
        self.dice_hand = dicehand.DiceHand()
        
    def test_roll_dice_invalid_input_zero(self):
        with self.assertRaises(ValueError):
            self.dice_hand.roll_dice(0)
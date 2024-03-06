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
            
    def test_roll_dice_invalid_input_negative_float(self):
        with self.assertRaises(ValueError):
            self.dice_hand.roll_dice(-1.5)

    def test_roll_dice_invalid_input_positive_float(self):
        with self.assertRaises(TypeError):
            self.dice_hand.roll_dice(1.5)
            
    def test_roll_dice_invalid_input_letter(self):
        with self.assertRaises(TypeError):
            self.dice_hand.roll_dice('d')
            
    def test_roll_dice_invalid_input_None(self):
        with self.assertRaises(TypeError):
            self.dice_hand.roll_dice(None)
            
    def test_roll_dice_invalid_input_true_boolean(self):
        with self.assertRaises(TypeError):
            self.dice_hand.roll_dice(True)

    def test_roll_dice_invalid_input_false_boolean(self):
        with self.assertRaises(TypeError):
            self.dice_hand.roll_dice(False)
            
    def test_roll_dice_count_matches_result_count(self):
        num_rolls = 100
        rolls = self.dice_hand.roll_dice(num_rolls)
        self.assertEqual(len(rolls), num_rolls)
                     
if __name__ == '__main__':
    unittest.main()
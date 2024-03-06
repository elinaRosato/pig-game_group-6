import unittest
import dice

class TestDice(unittest.TestCase):
    
     def setUp(self):
        self.dice = dice.Dice()
        
     def test_roll_result_not_null(self):
        result = self.dice.roll()
        self.assertIsNotNone(result)
        
if __name__ == '__main__':
    unittest.main()
import unittest
import dice

class TestDice(unittest.TestCase):
    
     def setUp(self):
        self.dice = dice.Dice()
        
     def test_roll_result_not_null(self):
        result = self.dice.roll()
        self.assertIsNotNone(result)
        
     def test_roll_result_within_range(self):
        for _ in range(100):
            result = self.dice.roll()
            self.assertIsNotNone(result)
            self.assertTrue(1 <= result <= 6)
        
if __name__ == '__main__':
    unittest.main()
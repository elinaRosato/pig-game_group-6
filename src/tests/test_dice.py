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
            
    def test_roll_result_in_any_of_possible_output_values(self):
        possible_values = [1, 2, 3, 4, 5, 6]
        for _ in range(100):
            result = self.dice.roll()
            self.assertIsNotNone(result)
            self.assertIn(result, possible_values)
            
    def test_roll_is_return_type_int(self):
        result = self.dice.roll()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, int))
        
    def test_roll_upper_value_limit(self):
        for _ in range(100):
            result = self.dice.roll()
            self.assertIsNotNone(result)
            self.assertLessEqual(result, 6)
            
    def test_roll_lower_value_limit(self):
        for _ in range(100):
            result = self.dice.roll()
            self.assertIsNotNone(result)
            self.assertGreaterEqual(result, 1)
            
    def test_roll_ensure_all_dice_numbers_are_thrown(self):
        results = [self.dice.roll() for _ in range(100)]
        self.assertIsNotNone(results)
        unique_results = set(results)
        self.assertGreater(len(unique_results), 1)
            
    
        
if __name__ == '__main__':
    unittest.main()
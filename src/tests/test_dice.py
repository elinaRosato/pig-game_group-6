import unittest
import random
from game.dice import Dice

class TestDice(unittest.TestCase):
    
    def setUp(self):
        self.dice = Dice()
        
    def test_roll_result_not_null(self):
        """Test that the result of rolling the dice is not null."""
        result = self.dice.roll()
        self.assertIsNotNone(result)
        
    def test_roll_result_within_range(self):
        """Test that when rolling the dice the result is within range 1 and 6 (both inclusive)."""
        for _ in range(100):
            result = self.dice.roll()
            self.assertIsNotNone(result)
            self.assertTrue(1 <= result <= 6)
            
    def test_roll_result_in_any_of_possible_output_values(self):
        """Test that the result is identical to any of the values provided by the possible_values list."""
        possible_values = [1, 2, 3, 4, 5, 6]
        for _ in range(100):
            result = self.dice.roll()
            self.assertIsNotNone(result)
            self.assertIn(result, possible_values)
            
    def test_roll_is_return_type_int(self):
        """Test that return type of rolling the dice is integer."""
        result = self.dice.roll()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, int))
        
    def test_roll_upper_value_limit(self):
        """Test that after rolling the dice specified amount of times, the maximum value is 6."""
        for _ in range(100):
            result = self.dice.roll()
            self.assertIsNotNone(result)
            self.assertLessEqual(result, 6)
            
    def test_roll_lower_value_limit(self):
        """Test that after rolling the dice specified amount of times, the minimum value is 1."""
        for _ in range(100):
            result = self.dice.roll()
            self.assertIsNotNone(result)
            self.assertGreaterEqual(result, 1)
            
    def test_roll_ensure_all_dice_numbers_are_thrown(self):
        """Test that after rolling a dice specified amount of times,
           6 different numbers (from 1-6) have been rolled."""
        results = [self.dice.roll() for _ in range(100)]
        self.assertIsNotNone(results)
        unique_results = set(results)
        self.assertEqual(len(unique_results), 6)
        
    def test_roll_count_matches_results_count(self):
        """Test that length of the results list is equal to the expected number of rolls (num_rolls)."""
        num_rolls = 10
        results = [self.dice.roll() for _ in range(num_rolls)]
        self.assertIsNotNone(results)
        self.assertEqual(len(results), num_rolls)
            
    def test_roll_numbers_are_uniformly_represented(self):
        """Test that all dice numbers (from 1 to 6) are evenly represented in specified number of rolls."""
        num_rolls = 100
        results = [self.dice.roll() for _ in range(num_rolls)]
        self.assertIsNotNone(results)
        for value in range(1, 7):
            occurrence = results.count(value)
            self.assertLessEqual(occurrence, num_rolls * 0.5)
    
    def test_reproducible_results_with_fixed_seed(self):
        """This is a negative test with a fixed seed where we check
        that the 'random' method behaviour stops being random due to
        a fixed seed value."""
        seed = 32
        random.seed(seed)
        result1 = self.dice.roll()
        self.assertIsNotNone(result1)
        random.seed(seed)
        result2 = self.dice.roll()
        self.assertIsNotNone(result2)
        self.assertEqual(result1, result2)
        
if __name__ == '__main__':
    unittest.main()
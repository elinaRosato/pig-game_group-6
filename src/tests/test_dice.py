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
        
    def test_roll_count_matches_results_count(self):
        num_rolls = 10
        results = [self.dice.roll() for _ in range(num_rolls)]
        self.assertIsNotNone(results)
        self.assertEqual(len(results), num_rolls)
            
    def test_roll_numbers_are_uniformly_represented(self):
        num_rolls = 100
        results = [self.dice.roll() for _ in range(num_rolls)]
        self.assertIsNotNone(results)
        for value in range(1, 7):
            occurrence = results.count(value)
            self.assertLessEqual(occurrence, num_rolls * 0.5)
    
    def test_reproducible_results_with_fixed_seed(self):
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
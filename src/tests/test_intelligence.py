import unittest

class TestIntelligence(unittest.TestCase):

    # Valid Intelligence Initialization
    def test_valid_intelligence_initialization_default(self):
        """
        Test creating an Intelligence instance with a valid default difficulty.
        """
        intelligence_instance = Intelligence()
        self.assertEqual(intelligence_instance.difficulty, "medium")

    def test_valid_intelligence_initialization_easy(self):
        """
        Test creating an Intelligence instance with a valid easy difficulty.
        """
        intelligence_instance = Intelligence("easy")
        self.assertEqual(intelligence_instance.difficulty, "easy")
   
    def test_valid_intelligence_initialization_medium(self):
        """
        Test creating an Intelligence instance with a valid medium difficulty.
        """
        intelligence_instance = Intelligence("medium")
        self.assertEqual(intelligence_instance.difficulty, "medium")

    def test_valid_intelligence_initialization_hard(self):
        """
        Test creating an Intelligence instance with a valid hard difficulty.
        """
        intelligence_instance = Intelligence("hard")
        self.assertEqual(intelligence_instance.difficulty, "hard")
    
    # Invalid Intelligence Initialization
    def test_invalid_intelligence_initialization_type(self):
        """
        Test creating an Intelligence instance with an invalid difficulty type and expect a TypeError.
        """
        # Test case 1: Invalid level type (integer)
        with self.assertRaises(TypeError):
            intelligence_instance = Intelligence(123)

        # Test case 2: Invalid level type (float)
        with self.assertRaises(TypeError):
            intelligence_instance = Intelligence(1.23)
        
        # Test case 3: Invalid level type (boolean)
        with self.assertRaises(TypeError):
            intelligence_instance = Intelligence(False)

    def test_invalid_intelligence_initialization_value(self):
        """
        Test creating an Intelligence instance with an invalid difficulty value and expect a ValueError.
        """
        # Test case 1: Invalid level type (empty string)
        with self.assertRaises(ValueError):
            intelligence_instance = Intelligence("")

        # Test case 2: Invalid level type (invalid string)
        with self.assertRaises(ValueError):
            intelligence_instance = Intelligence("difficult")

if __name__ == '__main__':
    unittest.main()
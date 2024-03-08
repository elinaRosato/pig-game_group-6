import unittest
from intelligence import Intelligence

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
        # Test case 1: Invalid difficulty type (integer)
        with self.assertRaises(TypeError):
            _ = Intelligence(123)

        # Test case 2: Invalid difficulty type (float)
        with self.assertRaises(TypeError):
            _ = Intelligence(1.23)

        # Test case 3: Invalid difficulty type (boolean)
        with self.assertRaises(TypeError):
            _ = Intelligence(False)

    def test_invalid_intelligence_initialization_value(self):
        """
        Test creating an Intelligence instance with an invalid difficulty value and expect a ValueError.
        """

        # Test case 1: Invalid difficulty type (empty string)
        with self.assertRaises(ValueError):
            _ = Intelligence("")

        # Test case 2: Invalid difficulty type (invalid string)
        with self.assertRaises(ValueError):
            _ = Intelligence("difficult")

    # Set difficulty method with valid and invalid values
    def test_set_difficulty_valid(self):
        """
        Test setting a valid difficulty.
        """
        intelligence_instance = Intelligence()
        intelligence_instance.set_difficulty("hard")
        self.assertEqual(intelligence_instance.difficulty, "hard")

    def test_set_difficulty_invalid_type(self):
        """
        Test setting an invalid difficulty type and expect a TypeError.
        """
        intelligence_instance = Intelligence()

        # Test case 1: Invalid difficulty type (integer)
        with self.assertRaises(TypeError):
            intelligence_instance.set_difficulty(123)

        # Test case 2: Invalid difficulty type (float)
        with self.assertRaises(TypeError):
            intelligence_instance.set_difficulty(1.23)

        # Test case 3: Invalid difficulty type (boolean)
        with self.assertRaises(TypeError):
            intelligence_instance.set_difficulty(True)

    def test_set_difficulty_invalid_value(self):
        """
        Test setting an invalid difficulty value and expect a ValueError.
        """
        intelligence_instance = Intelligence()

        # Test case 1: Invalid difficulty type (empty string)
        with self.assertRaises(ValueError):
            intelligence_instance.set_difficulty("")

        # Test case 2: Invalid difficulty type (invalid string)
        with self.assertRaises(ValueError):
            intelligence_instance.set_difficulty("difficult")

    # Choose turns method with valid and invalid values
    def test_choose_turns_easy(self):
        """
        Test choosing turns for easy difficulty.
        """
        intelligence_instance = Intelligence("easy")
        turns = intelligence_instance.choose_turns()
        self.assertIn(turns, [1, 2])

    def test_choose_turns_medium(self):
        """
        Test choosing turns for medium difficulty.
        """
        intelligence_instance = Intelligence("medium")
        turns = intelligence_instance.choose_turns()
        self.assertIn(turns, [1, 2, 3])

    def test_choose_turns_hard(self):
        """
        Test choosing turns for hard difficulty.
        """
        intelligence_instance = Intelligence("hard")
        turns = intelligence_instance.choose_turns()
        self.assertIn(turns, [2, 3, 4])

if __name__ == '__main__':
    unittest.main()
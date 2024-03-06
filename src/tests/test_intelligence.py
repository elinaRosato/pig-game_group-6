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

if __name__ == '__main__':
    unittest.main()
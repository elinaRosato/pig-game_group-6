import unittest
from unittest.mock import patch
from game import Game
import os

class TestGame(unittest.TestCase):
        
    def setUp(self):
        self.game = Game()
        
    def tearDown(self):
        #We need this to reset the file of highscores and avoid conflicts with existing names from previous test executions.
        filename = "highscores.json"
        if os.path.exists(filename):
            os.remove(filename)    

    # Game Initialization
    def test_game_initialization(self):
        """
        Test the initialization of the Game class.
        """
        game = Game()
        self.assertIsNotNone(game.dice_hand)
        self.assertIsNotNone(game.high_score)
        self.assertIsNotNone(game.player1)
        self.assertIsNotNone(game.player2)
        self.assertIsNotNone(game.intelligence)
        self.assertIsNotNone(game.histogram)
    
    # Get player name
    def test_get_player_name(self):
        """
        Test the get_player_name method.

        Mocks the input function to provide the name 'John'.
        Checks if the player1's name is correctly set to 'John'.
        """
        with patch('builtins.input', side_effect=['John']):
            self.game.get_player_name()
        self.assertEqual(self.game.player1.name, 'John')

    # Change player name
    def test_change_player_name(self):
        """
        Test the change_player_name method.

        Sets the player1's name to 'Sarah', updates highscores with the old name,
        mocks the input to change the name to 'Peter', and checks if the player1's
        name is correctly updated to 'Peter'.
        """
        self.game.player1.change_name("Sarah")
        
        self.game.high_score.update_highscores("Sarah", 0) 
        
        with patch('builtins.input', side_effect=['yes', 'Peter']):
            self.game.change_player_name()
        
        self.assertEqual(self.game.player1.name, 'Peter')
        
    # Set computer opponent
    def test_set_computer_opponent_with_valid_difficulty(self):
        """
        Test the set_computer_opponent method with a valid difficulty.

        Mocks the input to choose 'easy' difficulty for the computer opponent.
        Checks if player2 is marked as a computer and if the intelligence difficulty is set correctly.
        """
        with patch('builtins.input', side_effect=['easy']):
            self.game.set_computer_opponent()
        self.assertTrue(self.game.player2.is_computer)
        self.assertEqual(self.game.intelligence.difficulty, ['easy', 'medium', 'hard'])

    # Set human oponent
    def test_set_human_opponent(self):
        """
        Test the set_human_opponent method.

        Mocks the input to provide the opponent's name as 'Benjamin'.
        Checks if player2's name is correctly set to 'Benjamin'.
        """
        with patch('builtins.input', return_value='Benjamin'):
            self.game.set_human_opponent()
        self.assertEqual(self.game.player2.name, 'Benjamin')
    

if __name__ == '__main__':
    unittest.main()
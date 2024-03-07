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
        
    def test_get_player_name(self):
        with patch('builtins.input', side_effect=['John']):
            self.game.get_player_name()
        self.assertEqual(self.game.player1.name, 'John')

    def test_change_player_name(self):
        self.game.player1.change_name("Sarah")
        
        self.game.high_score.update_highscores("Sarah", 0) 
        
        with patch('builtins.input', side_effect=['yes', 'Peter']):
            self.game.change_player_name()
        
        self.assertEqual(self.game.player1.name, 'Peter')

if __name__ == '__main__':
    unittest.main()
import unittest
from unittest.mock import patch
from game import Game

class TestGame(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()
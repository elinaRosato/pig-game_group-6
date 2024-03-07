import unittest
from unittest.mock import patch
from game import Game
import os
import sys
from io import StringIO

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
        
    def test_play_round_2_human_players(self):
        # Prepare predefined inputs for player decision
        player1_inputs = ['roll', '1', 'hold']
        player2_inputs = ['roll', '1', 'cheat']

        # Redirect stdout to a StringIO object to capture printed output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Set up patch for builtins.input
        with patch('builtins.input', side_effect=player1_inputs + player2_inputs):
            # Test playing a round
            self.game.player1.name = "Player1"
            self.game.player2.name = "Player2"
            self.game.play_round(self.game.player1, self.game.player2)

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Get the captured output
        output = captured_output.getvalue()

        # Assert that the output contains expected messages
        self.assertIn("Player1's turn:", output)
        self.assertIn("Player1 rolled:", output)

        if "Player1 rolled a 1!" in output:
              self.assertIn("Turn over.", output)
        else:
            self.assertIn("Player1's score:", output)
            self.assertIn("Player2's turn:", output)
            if "Player2 rolled a 1!" in output:
                self.assertIn("Turn over.", output)
            else:
                self.assertIn("Player2 rolled:", output)
                self.assertIn("Cheat activated! Setting your score to 100.", output)
                self.assertIn("score: 100", output)
                self.assertIn("You win!", output)
        
    # Choosing to cheat against the computer
    def test_play_cheat_against_computer(self):
        """
        Test playing the game against the computer, choosing to cheat, and confirming the game ends.
        """
        with patch('builtins.input', side_effect=['Veronica', 'no', 'yes', 'medium', 'cheat', 'no']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.game.play()
                output = mock_stdout.getvalue()
                self.assertIn("Welcome to Pig! The Hog variant", output)
                self.assertIn("Cheat activated! Setting your score to 100.", output)
                self.assertIn("Thanks for playing!", output)
    
    # Choosing to cheat against a real player
    def test_play_cheat_against_human(self):
        """
        Test playing the game against a human, choosing to cheat, and confirming the game ends.
        """
        with patch('builtins.input', side_effect=['Karen', 'no', 'no', 'Jimmy', 'no', 'cheat', 'no']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.game.play()
                output = mock_stdout.getvalue()
                self.assertIn("Welcome to Pig! The Hog variant", output)
                self.assertIn("Cheat activated! Setting your score to 100.", output)
                self.assertIn("Thanks for playing!", output) 
    
    def test_play_histogram_invalid_against_person(self):
        """
        Test playing the game against a human, choosing to display the histogram with an invalid input,
        cheating, and confirming the game ends.
        """
        with patch('builtins.input', side_effect=['Gabriella', 'no', 'no', 'Harry', 'no', 'histogram', 'invalid', 'cheat', 'no']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.game.play()
                output = mock_stdout.getvalue()
                self.assertIn("Welcome to Pig! The Hog variant", output)
                self.assertIn("Invalid input. Please enter a valid option.", output)
                self.assertIn("Thanks for playing!", output)
    

if __name__ == '__main__':
    unittest.main()
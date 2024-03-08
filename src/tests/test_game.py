import unittest
from unittest.mock import patch
from game import Game
import os
import sys
from io import StringIO

class TestGame(unittest.TestCase):
        
    def setUp(self):
        self.game = Game()
        
    #We need this to reset the file of highscores and avoid conflicts with existing names from previous test executions.
    def tearDown(self):
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
        """
        with patch('builtins.input', side_effect=['John']):
            self.game.get_player_name()
        self.assertEqual(self.game.player1.name, 'John')

    def test_get_player_name_empty_input(self):
        """
        Test handling an empty string input in get_player_name method.
        """
        with patch('builtins.input', side_effect=['', 'Victoria']):
            self.game.get_player_name()
        self.assertEqual(self.game.player1.name, 'Victoria')

    # Change player name
    def test_change_player_name(self):
        """
        Test the change_player_name method.
        """
        self.game.player1.change_name("Sarah")
        
        self.game.high_score.update_highscores("Sarah", 0) 
        
        with patch('builtins.input', side_effect=['yes', 'Peter']):
            self.game.change_player_name()
        
        self.assertEqual(self.game.player1.name, 'Peter')
    
    def test_change_player_name_empty_input(self):
        """
        Test handling an empty string input in change_player_name method.
        """
        self.game.player1.change_name("Dora")
        self.game.high_score.update_highscores("Dora", 0)
        
        with patch('builtins.input', side_effect=['yes', '']):
            self.game.change_player_name()
        
        self.assertEqual(self.game.player1.name, 'Dora')
    
    # Set computer opponent
    def test_set_computer_opponent_with_valid_difficulty(self):
        """
        Test the set_computer_opponent method with a valid difficulty.
        """
        with patch('builtins.input', side_effect=['easy']):
            self.game.set_computer_opponent()
        self.assertTrue(self.game.player2.is_computer)
        self.assertEqual(self.game.intelligence.difficulty, ['easy', 'medium', 'hard'])

    # Set human oponent
    def test_set_human_opponent(self):
        """
        Test the set_human_opponent method.
        """
        with patch('builtins.input', return_value='Benjamin'):
            self.game.set_human_opponent()
        self.assertEqual(self.game.player2.name, 'Benjamin')
        
    def test_play_round_2_human_players(self):
        """
        Test the play_round method with two human players.
        """
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
    
    def test_take_turn_computer(self):
        """
        Test with player2 being the computer. The intelligence returns 2 rolls and then
        we check that the score is correct.
        """
        self.game.player2.is_computer = True
        with patch.object(self.game.intelligence, 'choose_turns', return_value=2):
            with patch.object(self.game.dice_hand, 'roll_dice', return_value=[3, 4]):
                score = self.game.take_turn(self.game.player2)
        self.assertEqual(score, 7)

    def test_take_turn_computer_roll_1(self):
        """
        Test with player2 being the computer. The intelligence returns 2 rolls but one
        of them is 1, so the score for that turn is 0.
        """
        self.game.player2.is_computer = True
        with patch.object(self.game.intelligence, 'choose_turns', return_value=2):
            with patch.object(self.game.dice_hand, 'roll_dice', return_value=[1,3]):
                score = self.game.take_turn(self.game.player2)
        self.assertEqual(score, 0)

    # Play again
    @patch('builtins.input', side_effect=['yes'])
    def test_play_again_yes(self):
        """
        Test that play_again returns True when the player enters 'yes'.
        """
        result = self.game.play_again()
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['no'])
    def test_play_again_no(self):
        """
        Test that play_again returns False when the player enters 'no'.
        """
        result = self.game.play_again()
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['invalid', 'yes'])
    def test_play_again_invalid_then_yes(self):
        """
        Test that play_again handles invalid input and returns True when the player eventually enters 'yes'.
        """
        result = self.game.play_again()
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['invalid', 'another_invalid', 'no'])
    def test_play_again_invalid_then_another_invalid_then_no(self):
        """
        Test that play_again handles multiple invalid inputs and returns False when the player eventually enters 'no'.
        """
        result = self.game.play_again()
        self.assertFalse(result)
   
        
        
if __name__ == '__main__':
    unittest.main()